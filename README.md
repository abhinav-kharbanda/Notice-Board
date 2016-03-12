# Notice-Board
Digital Kiosk Notice Board Display for College

## Installation

1. Setup Notice Board App and its database

```
cd NoticeBoardApp-master
python manage.py makemigrations NoticeBoard
python manage.py migrate
```

2. Create Admin username and password

```
python manage.py createsuperuser
```
3. Execute the server - You can change the port and IP

```
python manage.py runserver 0.0.0.0:8000
```` 
4. Execute install.sh with sudo priviledge (Optional :  if you want to boot raspberrypi with the Kiosk displayed automatically).

```
chmod +x install.sh
sudo ./install.sh
```


Protected under GPLv3. Copyright of Abhinav Kharbanda 
