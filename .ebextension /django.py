﻿packages: 
  yum:
    python3-devel: []
    mariadb-devel: []

option_settings:
   aws:elasticbeanstalk:container:python:
     WSGIPath: Attendance_System.wsgi:application
   aws:elasticbeanstalk:environment:proxy:staticfiles:
    /static: static
