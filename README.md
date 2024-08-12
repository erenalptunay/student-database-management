# **Student Database Management System**

_This document is also available in Turkish below._  
_Bu belgenin Türkçe versiyonu aşağıda mevcuttur._


## **About the Project:**
_This project is a database management system developed to track the information and course grades of students in a university._ 
_Database operations are performed using SQLAlchemy, and basic operations related to students (add, update, delete) and management of course grades are provided through this system._

## **Database Schema:**


- **Students:** _Stores basic information of students (id, first name, last name, student number, department). Each student has a unique student number._


- **Lessons:** _Contains information about the courses at the university (id, course name, course code). Each course has its own code._


- **Grades:** _Holds the relationship between students and courses. This table shows which grade a student received in a particular course and is linked to the student and course tables via ForeignKey._

## **File Structure and Responsibilities:**

- **main.py:** _Manages the interaction between the user and the system. It initiates the appropriate operations based on the user input by calling the functions in the operations.py file. Through the main menu options, the user can perform various operations on students and course grades._


- **operations.py:** _Contains functions that perform various operations on the database. Through these functions, you can add, update, delete students, and add or update course grades. It also includes functions to delete a student's grade for a particular course and list the grades._


- **models.py:** _Defines the database schema and sets the relationships between tables. This file is where the student, course, and grade tables are defined. The database connection is established here, and the creation of tables is facilitated._


- **setup.py:** _This script facilitates the rapid setup of the project by installing dependencies and performing necessary configurations. It prepares the project package for installation and executes additional setup steps as required. Specifically, it sets up the database and loads the departments and lessons data._


## **Functions:**

- _Add Student: Creates a new student record._


- _Update Student: Updates the information of an existing student._


- _Delete Student: Removes a student record from the database._


- _Add Grade: Adds a grade for a specific course for a student._


- _Update Grade: Updates an existing course grade for a student._


- _Delete Grade: Deletes a student's grade for a specific course._


- _Get Student Grade: Lists a student's grades for all courses._

This system provides the basic functions of student information systems in universities in a simplified manner. 
It offers an understandable structure for users who want to grasp database operations and makes data management straightforward. 
The three main Python files of the system interact with the database based on user requests to manage student and grade information.

## **Setup:**

**Download the Project:** 
Use the following command in your terminal or command prompt to clone the project to your computer from GitHub:

### `git clone https://github.com/USERNAME/REPO.git`

Replace `USERNAME` and `REPOSITORY` with the appropriate GitHub username and project name.
Alternatively, you can download it as a ZIP file from GitHub and extract it.

**Navigate to the Project Directory:** 
Move to the directory where the project files are located:

### `cd REPOSITORY`

**Install Required Libraries:**

Install Python Libraries: Open the terminal or command prompt in the project directory and run the following command to install the necessary Python libraries:

### `pip install -r requirements.txt`

**Create the Database and Load Data:**
Run the setup file to create the database and load the necessary data:

### `python setup.py`

**Run the Application:**
To start the application, run the following command in the terminal:

### `python main.py`

### **Setup with Docker (Optional):**

_You can run the project in an isolated environment using Docker._

**Install Docker and Docker Compose:** 
Install Docker and Docker Compose on your system. Follow the installation guides to complete the installations.

**Build Docker Image:** 
Open the terminal in the directory where your project files are located and run the following command to build the Docker image:

### `docker-compose build`

**Start Docker Container:** 
After building the image, start the container by typing the following command in the terminal:

### `docker-compose up`

**nteractive Terminal Usage:**
If your application requires interactive terminal input, you can start your Docker container in interactive mode using the following command.

### `docker-compose run app`

When setting up with Docker, the project runs inside a container, and the database along with other dependencies are automatically configured.


# Türkçe 

# **Öğrenci Veritabanı Yönetim Sistemi**


## **Proje Hakkında:**
_Bu proje, bir üniversitedeki öğrencilerin bilgilerini ve ders notlarını takip etmek amacıyla geliştirilmiş bir veritabanı yönetim sistemidir._ 
_SQLAlchemy ile veritabanı işlemleri yapılmakta olup, öğrencilerle ilgili temel işlemler (ekleme, güncelleme, silme) ve ders notlarının yönetimi bu sistem üzerinden sağlanmaktadır._


## **Veritabanı Şeması:**

- **Students (Öğrenciler):** _Öğrencilerin temel bilgilerini (id, isim, soyisim, öğrenci numarası, bölüm) tutar. Her öğrenciye ait benzersiz bir öğrenci numarası bulunur._


- **Lessons (Dersler):** _Üniversitedeki derslerin bilgilerini (id, ders adı, ders kodu) içerir. Her dersin kendine ait bir kodu vardır._


- **Grades (Notlar):** _Öğrenci ve dersler arasındaki ilişkiyi tutar. Bu tablo, hangi öğrencinin hangi dersten kaç aldığını gösterir ve öğrenci ile ders tablolarına ForeignKey ile bağlıdır._



## **Dosya Yapısı ve Görevleri:**

- **main.py:** _Kullanıcı ile sistem arasındaki etkileşimi sağlar. Kullanıcıdan alınan girdilere göre uygun işlemleri başlatarak operations.py dosyasındaki fonksiyonları çağırır. Ana menüde sunulan seçenekler ile kullanıcı, öğrenciler ve ders notları üzerinde çeşitli işlemleri gerçekleştirebilir._


- **operations.py:** _Veritabanı üzerinde çeşitli işlemleri gerçekleştiren fonksiyonlar içerir. Bu fonksiyonlar aracılığıyla öğrenci ekleme, güncelleme, silme, ders notu ekleme ve güncelleme gibi işlemler yapılır. Ayrıca, bir öğrencinin belirli bir dersteki notunu silme ve notları listeleme gibi işlevler de bu dosyada bulunur._


- **models.py:** _Veritabanı şemasını tanımlayan ve tablo ilişkilerini belirleyen dosyadır. Öğrenci, ders ve not tabloları burada tanımlanır. Veritabanı bağlantısı bu dosyada kurulur ve tabloların oluşturulması sağlanır._


- **setup.py:** _Bu betik, projeyi hızlı bir şekilde kurmayı sağlar; bağımlılıkları yükler ve gerekli yapılandırmaları gerçekleştirir. Proje paketini kurulum için hazırlar ve gerektiğinde ek kurulum adımlarını uygular. Özellikle, veritabanını kurar ve bölümler ile ders verilerini yükler._


## **İşlevler:**

- _Öğrenci Ekleme: Yeni bir öğrenci kaydı oluşturur._


- _Öğrenci Güncelleme: Mevcut bir öğrencinin bilgilerini günceller._


- _Öğrenci Silme: Veritabanından bir öğrenci kaydını siler._


- _Ders Notu Ekleme: Belirli bir öğrenci için bir dersin notunu ekler._


- _Ders Notu Güncelleme: Öğrencinin mevcut bir ders notunu günceller._


- _Ders Notu Silme: Bir öğrencinin belirli bir dersten aldığı notu siler._


- _Notları Görüntüleme: Öğrencinin tüm derslerindeki notları listeler._

Bu sistem, üniversitelerdeki öğrenci bilgi sistemlerinin temel işlevlerini sade bir şekilde sunar. 
Veritabanı işlemlerini anlamak isteyen kullanıcılar için anlaşılır bir yapı sunar ve aynı zamanda veri yönetimini basit hale getirir.
Sistemin üç ana Python dosyası, kullanıcıdan gelen talepler doğrultusunda veritabanı ile etkileşime geçerek öğrenci ve not bilgilerini yönetir.

## **Kurulum:**


**Projeyi İndirin:** 
GitHub'dan projeyi bilgisayarınıza klonlamak için terminal veya komut istemcisinde aşağıdaki komutu kullanın:


### `git clone https://github.com/USERNAME/REPO.git`


Bu komutta USERNAME ve REPOSITORY yerlerine uygun GitHub kullanıcı adı ve proje adıyla değiştirilmelidir.
Alternatif olarak, GitHub'dan ZIP dosyası olarak da indirebilir ve çıkartabilirsiniz.

**Proje Dizinine Girin:** 
Proje dosyalarının bulunduğu dizine geçin:


### `cd REPOSITORY`


**Gerekli Kütüphaneleri Kurun:**

Python Kütüphanelerini Yükleyin: Proje dizininde terminal veya komut istemcisini açın ve gerekli Python kütüphanelerini yüklemek için aşağıdaki komutu çalıştırın:


### `python main.py`


### `pip install -r requirements.txt`

**Veritabanını ve Verileri Oluşturun:**
Kurulum dosyasını çalıştırarak veritabanını oluşturun ve gerekli verileri yükleyin:


### `python setup.py`


**Uygulamayı Başlatın:**
Uygulamayı başlatmak için terminalde aşağıdaki komutu çalıştırın:


### `python main.py`


### **Docker ile Kurulum (Opsiyonel):**

_Docker kullanarak projeyi izole bir ortamda çalıştırabilirsiniz._ 


**Docker ve Docker Compose Kurulumu:** 
Docker'ı ve Docker Compose'u sisteminize kurun. Kurulum kılavuzlarını takip ederek kurulumları tamamlayın.

**Docker İmajını Oluşturma:** 
Proje dosyalarınızın bulunduğu dizinde terminali açın ve Docker imajını oluşturmak için aşağıdaki komutu çalıştırın:


### `docker-compose build`

**Docker Konteynerini Başlatma:** 
İmaj oluşturduktan sonra konteyneri başlatmak için terminale şu komutu yazın:

### `docker-compose up`

**Etkileşimli Terminal Kullanımı:**
Eğer uygulamanız etkileşimli bir terminal girişi gerektiriyorsa, Docker konteynerinizi etkileşimli modda başlatmak için aşağıdaki komutu kullanabilirsiniz.


### `docker-compose run app`

Docker ile kurulum yapıldığında, proje konteyner içinde çalışır ve veritabanı ile diğer bağımlılıklar otomatik olarak yapılandırılır.

