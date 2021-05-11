from flask import Flask, render_template, request, url_for, make_response, session, redirect, flash
from flask_login import login_required, current_user
from mysql_db import MySQL
import mysql.connector as connector
import math

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

mysql = MySQL(app)

from auth import bp as auth_bp, init_login_manager, check_rights

init_login_manager(app)
app.register_blueprint(auth_bp)
PER_PAGE = 5

def load_genres():
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT id, name FROM exam_genres;')
    genres = cursor.fetchall()
    cursor.close()
    return genres

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reviews')
@check_rights('users_review')
@login_required
def users_review():
    user_id = getattr(current_user, 'id', None)
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT t1.name, t2.rating, t2.review_text, t2.date_added, t3.status FROM exam_films t1 JOIN exam_reviews t2 ON t1.id=t2.film_id JOIN exam_reviews_status t3 ON t3.id=t2.status_id WHERE user_id=%s and t1.id=t2.film_id;', (user_id,))
    reviews = cursor.fetchall()
    cursor.close()
    return render_template('reviews/review_user.html', reviews=reviews)

@app.route('/reviews/moderator')
@check_rights('moder_review')
@login_required
def moder_review():
    page = request.args.get('page', 1, type=int)
    with mysql.connection.cursor(named_tuple=True) as cursor:
        cursor.execute('SELECT count(t1.id) AS count FROM exam_reviews t1 JOIN exam_reviews_status t2 ON t1.status_id=t2.id WHERE t2.status="на рассмотрении";')
        total_count = cursor.fetchone().count
    total_pages = math.ceil(total_count/PER_PAGE)
    pagination_info = {
        'current_page': page,
        'total_pages': total_pages,
        'per_page': PER_PAGE
    }
    query = ''' 
        SELECT t2.id, t1.name, t2.date_added, t4.last_name, t4.first_name 
        FROM exam_films t1 JOIN exam_reviews t2 ON t1.id=t2.film_id JOIN exam_reviews_status t3 ON t3.id=t2.status_id JOIN exam_users t4 ON t4.id=t2.user_id 
        WHERE t1.id=t2.film_id and (t2.status_id IN (SELECT t3.id WHERE t3.status="на рассмотрении")) ORDER BY t2.date_added DESC LIMIT %s OFFSET %s;
    '''
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute(query, (PER_PAGE, PER_PAGE*(page-1)))
    reviews = cursor.fetchall()
    cursor.close()
    return render_template('reviews/moderator/review_moder.html', reviews=reviews, pagination_info=pagination_info)

@app.route('/films')
def films():
    page = request.args.get('page', 1, type=int)
    with mysql.connection.cursor(named_tuple=True) as cursor:
        cursor.execute('SELECT count(*) AS count FROM exam_films;')
        total_count = cursor.fetchone().count
    total_pages = math.ceil(total_count/PER_PAGE)
    pagination_info = {
        'current_page': page,
        'total_pages': total_pages,
        'per_page': PER_PAGE
    }
    query = '''
        SELECT id, name, description, production_year FROM exam_films ORDER BY production_year DESC LIMIT %s OFFSET %s;
        '''
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute(query, (PER_PAGE, PER_PAGE*(page-1)))
    films = cursor.fetchall()
    cursor.execute('SELECT t3.name AS g_name, t1.id as f_id FROM exam_films t1 JOIN exam_films_genres t2 ON t1.id=t2.film_id JOIN exam_genres t3 ON t2.genre_id=t3.id ;')
    genres = cursor.fetchall()
    cursor.execute('SELECT COUNT(t1.id) AS ct, t2.id FROM exam_reviews t1 JOIN exam_films t2 ON t1.film_id=t2.id WHERE t1.status_id IN (SELECT id FROM exam_reviews_status WHERE status="Одобренно") GROUP BY t2.id;')
    reviews = cursor.fetchall()
    cursor.close()
    return render_template('films/index.html', films=films, genres=genres, reviews=reviews, pagination_info=pagination_info)

@app.route('/films/<int:film_id>')
@check_rights('show')
@login_required
def show(film_id):
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM exam_films WHERE id = %s;', (film_id,))
    film = cursor.fetchone()
    cursor.execute('SELECT t1.review_text, t1.rating, t1.date_added, t2.last_name, t2.first_name FROM exam_reviews t1 JOIN exam_users t2 ON t1.user_id=t2.id WHERE ((film_id=%s) and t1.status_id IN (SELECT id FROM exam_reviews_status WHERE status="Одобренно"));', (film_id,))
    reviews = cursor.fetchall()
    cursor.execute('SELECT t3.name AS g_name, t1.id as f_id FROM exam_films t1 JOIN exam_films_genres t2 ON t1.id=t2.film_id JOIN exam_genres t3 ON t2.genre_id=t3.id ;')
    genres = cursor.fetchall()
    cursor.close()
    return render_template('films/show.html', film=film, reviews=reviews, genres=genres)


@app.route('/films/comment/<int:film_id>', methods=['POST', 'GET'])
@check_rights('show')
@login_required
def comment(film_id):
    cursor = mysql.connection.cursor(named_tuple=True)
    user_id = getattr(current_user, 'id', None)
    if request.method == "GET":
        return render_template('films/comments.html')
    if request.method == "POST":
        review_text = request.form.get('review_text')
        rating = (request.form.get('rating'))
        query = '''
                INSERT INTO exam_reviews (film_id, user_id, rating, review_text)
                VALUES (%s,%s,%s,%s);
                    '''    
        cursor.execute(query, (film_id, user_id, rating, review_text))        
        mysql.connection.commit()
        cursor.close()
        flash(f'Ваш отзыв был успешно добавлен.', 'success')
    return redirect(url_for('films'))


@app.route('/films/<int:film_id>/delete', methods=['POST'])
@check_rights('delete')
@login_required
def delete(film_id):
    with mysql.connection.cursor(named_tuple=True) as cursor:
        try:
            cursor.execute('DELETE FROM exam_films WHERE id = %s;', (film_id,))
        except connector.errors.DatabaseError:
            flash('Не удалось удалить запись.', 'danger')
            return redirect(url_for('films'))
        mysql.connection.commit()
        flash('Фильм был успешно удален.', 'success')
    return redirect(url_for('films'))

@app.route('/films/<int:film_id>/edit')
@check_rights('edit')
@login_required
def edit(film_id):
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM exam_films WHERE id = %s;', (film_id,))
    film = cursor.fetchone()
    cursor.close()
    return render_template('films/edit.html', film=film, genres=load_genres())

@app.route('/films/<int:film_id>/update', methods=['POST'])
@check_rights('edit')
@login_required
def update(film_id):
    name = request.form.get('name') or None
    description = request.form.get('description') or None
    production_year = request.form.get('production_year') or None
    country = request.form.get('country') or None
    director = request.form.get('director') or None
    screenwriter = request.form.get('screenwriter') or None
    actors = request.form.get('actors') or None
    duration = request.form.get('duration') or None
    # genre_id = request.form.get('genre_id') or None
    query = '''
        UPDATE exam_films SET name=%s, description=%s, production_year=%s, country=%s, director=%s, screenwriter=%s, actors=%s, duration=%s
        WHERE id=%s;
    '''
    cursor = mysql.connection.cursor(named_tuple=True)
    try:
        cursor.execute(query, (name, description, production_year, country, director, screenwriter, actors, duration, film_id))
    except connector.errors.DatabaseError:
        flash('Введены некорректные данные, ошибка сохранения', 'danger')
        film = {
            'id': film_id,
            'name': name,
            'description': description, 
            'production_year': production_year,
            'country': country,
            'director': director,
            'screenwriter': screenwriter,
            'actors': actors,
            'duration': duration
        }
        flash('Введены некорректные данные, ошибка сохранения', 'danger')
        return render_template('film/edit.html', film=film, genres=load_genres())
    mysql.connection.commit()
    cursor.close()
    flash(f'Фильм {name} был успешно обновлён.', 'success')
    return redirect(url_for('films'))


@app.route('/films/new')
@check_rights('new')
@login_required
def new():
    return render_template('films/new.html', film={}, genres=load_genres())

@app.route('/films/create', methods=['POST'])
@check_rights('new')
@login_required
def create():
    name = request.form.get('name') or None
    description = request.form.get('description') or None
    production_year = request.form.get('production_year') or None
    country = request.form.get('country') or None
    director = request.form.get('director') or None
    screenwriter = request.form.get('screenwriter') or None
    actors = request.form.get('actors') or None
    duration = request.form.get('duration') or None
    # genre_id = int(request.form.get('genre_id')) or None
    query = '''
        INSERT INTO exam_films (name, description, production_year, country, director, screenwriter, actors, duration)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    '''
    cursor = mysql.connection.cursor(named_tuple=True)
    try:
        cursor.execute(query, (name, description, production_year, country, director, screenwriter, actors, duration))
    except connector.errors.DatabaseError:
        flash('Введены некорректные данные, ошибка сохранения', 'danger')
        film = {
            'name': name,
            'description': description,
            'country': country,
            'director': director,
            'screenwriter': screenwriter,
            'actors': actors,
            'duration': duration
        }
        return render_template('films/new.html', film=film)
    cursor = mysql.connection.cursor(named_tuple=True)
    mysql.connection.commit()
    cursor.close()
    flash(f'Фильм {name} был успешно добавлен.', 'success')
    return redirect(url_for('films'))



@app.route('/reviews/moderator/<int:review_id>')
@check_rights('moder_review')
@login_required
def show_review(review_id):
    query = ''' 
        SELECT t2.id, t1.name, t2.date_added, t2.rating, t2.review_text, t4.last_name, t4.first_name 
        FROM exam_films t1 JOIN exam_reviews t2 ON t1.id=t2.film_id JOIN exam_reviews_status t3 ON t3.id=t2.status_id JOIN exam_users t4 ON t4.id=t2.user_id 
        WHERE t2.id=%s;
    '''
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute(query, (review_id,)) 
    reviews = cursor.fetchall()
    cursor.close()
    return render_template('reviews/moderator/show_review.html', reviews=reviews)

@app.route('/reviews/moderator/<int:review_id>/approve', methods=['POST', 'GET'])
@check_rights('moder_review')
@login_required
def approve(review_id):
    cursor = mysql.connection.cursor(named_tuple=True)
    if request.method == "POST":
        status = (request.form.get('status'))
        query = '''
            UPDATE exam_reviews SET status_id=%s
            WHERE id=%s;
        '''
        try:
            cursor.execute(query, (status, review_id ))
            mysql.connection.commit()
            cursor.close()
            flash(f'Статус рецензии был успешо изменен', 'success')
            return redirect(url_for('moder_review'))
        except connector.errors.DatabaseError:
            flash('Введены некорректные данные, ошибка сохранения', 'danger')
    return redirect(url_for('moder_review'))                