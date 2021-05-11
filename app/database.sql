-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: std-mysql    Database: std_1228_2
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `exam_films`
--

DROP TABLE IF EXISTS `exam_films`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam_films` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) NOT NULL,
  `description` text NOT NULL,
  `production_year` year(4) NOT NULL,
  `country` varchar(25) NOT NULL,
  `director` varchar(25) NOT NULL,
  `screenwriter` varchar(25) NOT NULL,
  `actors` varchar(255) NOT NULL,
  `duration` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam_films`
--

LOCK TABLES `exam_films` WRITE;
/*!40000 ALTER TABLE `exam_films` DISABLE KEYS */;
INSERT INTO `exam_films` VALUES (1,'Отпетые мошенницы','Как стать успешной мошенницей? Всегда будь во всеоружии: высокие каблуки, яркая помада и главное - утягивающее белье. Будь готова расплакаться в любой момент. Ни один мужчина не устоит перед женскими слезами. Бери все, что «плохо лежит» и хорошо блестит. За каждым миллионом может скрываться миллиард. Не откажи себе в удовольствии проверить.',2019,'США','Крис Эддисон',' Стэнли Шапиро','Энн Хэтэуэй, Ребел Уилсон, Алекс Шарп',93),(2,'Джентльмены','Один ушлый американец ещё со студенческих лет приторговывал наркотиками, а теперь придумал схему нелегального обогащения с использованием поместий обедневшей английской аристократии и очень неплохо на этом разбогател. Другой пронырливый журналист приходит к Рэю, правой руке американца, и предлагает тому купить киносценарий, в котором подробно описаны преступления его босса при участии других представителей лондонского криминального мира — партнёра-еврея, китайской диаспоры, чернокожих спортсменов и даже русского олигарха.',2019,' Великобритания, США','Гай Ричи',' Гай Ричи, Айван Эткинсон','Мэттью Макконахи, Чарли Ханнэм, Генри Голдинг',113),(3,'Выживший','Охотник Хью Гласс серьезно ранен на неизведанных просторах американского Дикого Запада. Товарищ Хью по отряду покорителей новых земель Джон Фицжеральд предательски оставляет его умирать в одиночестве. Теперь у Гласса осталось только одно оружие – его сила воли. Он готов бросить вызов первобытной природе, суровой зиме и враждебным племенам индейцев, только чтобы выжить и отомстить Фицжеральду.',2015,'США, Китай','Алехандро Гонсалес',' Марк Л. Смит',' Леонардо Ди Каприо,  Том Харди',156),(4,'Остров проклятых','Два американских судебных пристава отправляются на один из островов в штате Массачусетс, чтобы расследовать исчезновение пациентки клиники для умалишенных преступников. При проведении расследования им придется столкнуться с паутиной лжи, обрушившимся ураганом и смертельным бунтом обитателей клиники.',2010,'США','Мартин Скорсезе',' Лаэта Калогридис',' Леонардо Ди Каприо,  Марк Руффало',138),(5,'Чарли и шок. фабрика','Какие чудеса ждут вас на фабрике Вилли Вонки? Только представьте: травяные луга из сладкого мятного сахара в Шоколадной Комнате ... Можно проплыть по Шоколадной реке на розовой сахарной лодке ... Или поставить эксперименты в Комнате изобретений с леденцами, которые никогда не тают ... Понаблюдать за дрессированными белками в Ореховой Комнате или отправиться в стеклянном лифте в Телевизионную Комнату. Вы найдете слишком много смешного, чуть таинственного и настолько захватывающего в этом путешествии, что оно станет настолько же приятным и сладким для вас, как восхитительная сладкая палочка с розовой сливочной помадкой от Вилли Вонки.',2005,'США','Тим Бёртон',' Джон Огаст, Роальд Даль',' Джонни Депп,  Фредди Хаймор',115);
/*!40000 ALTER TABLE `exam_films` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exam_films_genres`
--

DROP TABLE IF EXISTS `exam_films_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam_films_genres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `film_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `film_id` (`film_id`),
  KEY `genre_id` (`genre_id`),
  CONSTRAINT `exam_films_genres_ibfk_1` FOREIGN KEY (`film_id`) REFERENCES `exam_films` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `exam_films_genres_ibfk_2` FOREIGN KEY (`genre_id`) REFERENCES `exam_genres` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam_films_genres`
--

LOCK TABLES `exam_films_genres` WRITE;
/*!40000 ALTER TABLE `exam_films_genres` DISABLE KEYS */;
INSERT INTO `exam_films_genres` VALUES (1,1,1),(2,1,2),(3,2,1),(4,2,3),(5,2,2),(6,3,4),(7,3,3),(8,3,6),(9,3,7),(10,4,6),(11,4,9),(12,4,5),(13,5,2),(14,5,8),(15,5,7),(16,5,10);
/*!40000 ALTER TABLE `exam_films_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exam_genres`
--

DROP TABLE IF EXISTS `exam_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam_genres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam_genres`
--

LOCK TABLES `exam_genres` WRITE;
/*!40000 ALTER TABLE `exam_genres` DISABLE KEYS */;
INSERT INTO `exam_genres` VALUES (4,' биография'),(3,' боевик'),(6,' драма'),(1,' преступление'),(8,' семейный'),(9,' триллер'),(10,' фэнтези'),(5,'детектив'),(2,'комедия'),(7,'приключения');
/*!40000 ALTER TABLE `exam_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exam_posters`
--

DROP TABLE IF EXISTS `exam_posters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam_posters` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file_name` varchar(100) NOT NULL,
  `mime_type` varchar(100) NOT NULL,
  `md5_hash` varchar(100) NOT NULL,
  `film_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `film_id` (`film_id`),
  CONSTRAINT `exam_posters_ibfk_1` FOREIGN KEY (`film_id`) REFERENCES `exam_films` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam_posters`
--

LOCK TABLES `exam_posters` WRITE;
/*!40000 ALTER TABLE `exam_posters` DISABLE KEYS */;
/*!40000 ALTER TABLE `exam_posters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exam_reviews`
--

DROP TABLE IF EXISTS `exam_reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam_reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `film_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `review_text` text NOT NULL,
  `date_added` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status_id` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `film_id` (`film_id`),
  KEY `status_id` (`status_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `exam_reviews_ibfk_1` FOREIGN KEY (`film_id`) REFERENCES `exam_films` (`id`) ON DELETE CASCADE,
  CONSTRAINT `exam_reviews_ibfk_2` FOREIGN KEY (`status_id`) REFERENCES `exam_reviews_status` (`id`) ON DELETE CASCADE,
  CONSTRAINT `exam_reviews_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `exam_users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam_reviews`
--

LOCK TABLES `exam_reviews` WRITE;
/*!40000 ALTER TABLE `exam_reviews` DISABLE KEYS */;
INSERT INTO `exam_reviews` VALUES (1,1,2,4,'Легкая дамская комедия, при просмотре которой меня не покидало чувство женского стыда. Но если не ждать чего-то интеллектуального, то вполне вероятно, что этот одноразовый фильм сможет вас развлечь.Как стать успешной мошенницей? Всегда будь во всеоружии: высокие каблуки, яркая помада и главное - утягивающее белье. В центре сюжета находятся две аферистки, которые уже давно привыкли получать деньги различными незаконными способами. Обе мошенницы предпочитают работать в одиночку.Но однажды их дороги пересекаются, и между ними возникает конфликт. Чтобы решить данный спор, девушки выбрали общую жертву. Они захотели устроить соревнование, чтобы определить, кто же из них лучше. Но в качестве жертвы они выбрали не простого человека. Они нацелились на юного гения, который уже смог заработать миллионы долларов.','2021-05-10 23:09:40',2),(2,1,1,3,'Почему решил посмотреть: комедия про аферисток\r\nВ итоге: в шестидесятых была комедия СКАЗКИ НА НОЧЬ; спустя четверть века, в конце восьмидесятых, сделали её культовый римейк со Стивом Мартином и Майклом Кейном. Прошло ещё тридцать лет, в Голливуде наступила эпоха победившего феминизма и теперь мы имеем очередную вариацию прославленной истории, на этот раз с двумя актрисами в главных ролях. В остальном сюжет не поменялся, шутки только стали попошлее.\r\nЖелая быть в тренде и снять кино с женщинами-главными героинями, создатели умудрились подтвердить худшие стереотипы о женщинах и их коварности и меркантильности.\r\nДочка смотрела с подружками, им понравилось.\r\nЯ не могу поставить больше, чем\r\n6(НЕПЛОХО) ','2021-05-10 23:09:40',2),(3,1,2,3,'сказать что то выдающееся, нет, такого нет, но раз посмотреть можно, ну или как фоновое кино поставить.','2021-05-10 23:13:36',2),(4,2,3,5,'О том, как трудно стало выйти на пенсию, даже если ты живёшь в Англии и торгуешь наркотой.\r\n\r\nГай Ричи решил снова снять бодрый боевичок о гангстерах и наркодельцах, тема-то по-прежнему модная, глядишь, и тоже Оскара подкинут. Хотя за шутку про черного урода теперь уже вряд ли. И жаль, ведь это самая злободневная часть фильма и его изюминка.\r\n\r\nМакконахи играет наркобарона, умного, принципиального да к тому же семьянина. Его попытка продать свой бизнес и выйти на пенсию всколыхнет преступный мир Лондона. А редактор местной газеты как раньше бывалыча пустит по его следу сыщика Хью Гранта.\r\n\r\nВ общем-то в фильме очень сложно обнаружить что-то новое. Да и тему с наркомафией кинематограф изъездил вдоль и поперек. Из нового тут только клоунские спортивные костюмы местного Макаренко Фарелла и его ко. Но вышло стильно. Причем, стиль плавно уходит в сторону от поднадоевшей Тарантиновщинв и приближается к чуть менее надоевшей Бессоновщине (ну очень приближается). Кого-то может разочарует, но, на мой взгляд, все к лучшему. Получилось кино для чуть более широкой аудитории.\r\n\r\nВ фильме практически нет абсурда, диалоги по существу, нет разглагольствований о ерунде. Хороший прием со сценарием (история внутри истории), на него можно списать любую неправдоподобность происходящего. В сюжете есть несколько кульбитов. Ричи сумел заинтриговать, но и не перемудрил. Драк немного, откровенно отвратительных сцен с вареньем нет совсем. Все очень пристойно, в 90-е бы сошло за семейное кино даже, но в 21 веке этот фильм имеет рейтинг 18+ даже несмотря на то, что семейным ценностям и проблемам воспитания и перевоспитания в нем уделяется даже больше внимания, пожалуй, чем в некоторых современных мультфильмах. Из откровенных глупостей - разве что отравление китайца шигеллой. Интересный взгляд на дизентерию, ничего не скажешь...\r\nНо, повторюсь, актеры хорошие, снято бодро. Так что посмотреть стоит. Даже если вам уже надоели фильмы про криминал и травку','2021-05-10 23:22:51',3),(5,3,3,5,'Фильм понравился игрой главного антагониста. Вот реально хорошо мужик играет. Крайне понравился демонстрацией суровой северной природы. Хорошо показывает, какие же мы, люди, все-таки песчинки в этом громадном мире.\r\nОбраз героя Ди-Каприо хорошо встроен в фильм, хотя ни капли не главный герой. Главный герой тут природа, в которой выживают единицы самых выносливых.','2021-05-10 23:23:24',2);
/*!40000 ALTER TABLE `exam_reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exam_reviews_status`
--

DROP TABLE IF EXISTS `exam_reviews_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam_reviews_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam_reviews_status`
--

LOCK TABLES `exam_reviews_status` WRITE;
/*!40000 ALTER TABLE `exam_reviews_status` DISABLE KEYS */;
INSERT INTO `exam_reviews_status` VALUES (1,'На рассмотрении'),(2,'Одобренно'),(3,'Отклонено');
/*!40000 ALTER TABLE `exam_reviews_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exam_roles`
--

DROP TABLE IF EXISTS `exam_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) NOT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam_roles`
--

LOCK TABLES `exam_roles` WRITE;
/*!40000 ALTER TABLE `exam_roles` DISABLE KEYS */;
INSERT INTO `exam_roles` VALUES (1,'администратор',NULL),(2,'модератор',NULL),(3,'пользователь',NULL);
/*!40000 ALTER TABLE `exam_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exam_users`
--

DROP TABLE IF EXISTS `exam_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(25) NOT NULL,
  `last_name` varchar(25) NOT NULL,
  `first_name` varchar(25) NOT NULL,
  `middle_name` varchar(25) DEFAULT NULL,
  `password_hash` varchar(256) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `login` (`login`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `exam_users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `exam_roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam_users`
--

LOCK TABLES `exam_users` WRITE;
/*!40000 ALTER TABLE `exam_users` DISABLE KEYS */;
INSERT INTO `exam_users` VALUES (1,'admin','Petrov','Petr','Petrovich','65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5','2021-05-10 22:23:01',1),(2,'user','Petrov','Ivan','Petrovich','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','2021-05-10 23:25:03',3),(3,'moder','Ivanov','Petr','Petrovich','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4','2021-05-10 23:25:15',2);
/*!40000 ALTER TABLE `exam_users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11 23:02:19
