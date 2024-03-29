# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 21:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_name', models.CharField(max_length=50)),
                ('link_description', models.CharField(blank=True, max_length=255)),
                ('link_url', models.URLField()),
                ('link_image', models.ImageField(upload_to='site_images/homepage/')),
                ('optional_class', models.CharField(blank=True, max_length=40)),
                ('placement', models.SmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_title', models.CharField(max_length=50)),
                ('icon', models.CharField(choices=[('aftereffects', 'Aftereffects'), ('angular', 'Angular'), ('apache', 'Apache'), ('autoit', 'Autoit'), ('babel', 'Babel'), ('backbone', 'Backbone'), ('bootstrap', 'Bootstrap'), ('bower', 'Bower'), ('bridge', 'Bridge'), ('browsersync', 'Browsersync'), ('c', 'C'), ('cassandra', 'Cassandra'), ('cockpit', 'Cockpit'), ('codeignitor', 'Codeignitor'), ('composer', 'Composer'), ('confluence', 'Confluence'), ('cplusplus', 'Cplusplus'), ('csharp', 'Csharp'), ('css-alt', 'Css-Alt'), ('css3', 'Css3'), ('css3-alt', 'Css3-Alt'), ('d3', 'D3'), ('database', 'Database'), ('debian', 'Debian'), ('default', 'Customer Icon'), ('dreamweaver', 'Dreamweaver'), ('drupal', 'Drupal'), ('dynamicweb', 'Dynamicweb'), ('ec3', 'Ec3'), ('ember', 'Ember'), ('emmet', 'Emmet'), ('express', 'Express'), ('fedora', 'Fedora'), ('fireworks', 'Fireworks'), ('flash', 'Flash'), ('freebsd', 'Freebsd'), ('git', 'Git'), ('git-squared', 'Git-Squared'), ('github', 'Github'), ('github-circle', 'Github-Circle'), ('github-circle-alt', 'Github-Circle-Alt'), ('gnome', 'Gnome'), ('google-code', 'Google-Code'), ('grails', 'Grails'), ('grailsalt', 'Grailsalt'), ('grunt', 'Grunt'), ('gulp', 'Gulp'), ('hadoop', 'Hadoop'), ('haskell', 'Haskell'), ('heroku', 'Heroku'), ('html5', 'Html5'), ('illustrator', 'Illustrator'), ('indesign', 'Indesign'), ('java', 'Java'), ('java-duke', 'Java-Duke'), ('jetty', 'Jetty'), ('jira', 'Jira'), ('jira-alt', 'Jira-Alt'), ('joomla', 'Joomla'), ('jquery', 'Jquery'), ('jquery-alt', 'Jquery-Alt'), ('js', 'JavaScript'), ('kde', 'Kde'), ('laravel', 'Laravel'), ('laravel-alt', 'Laravel-Alt'), ('less', 'Less'), ('lightroom', 'Lightroom'), ('linux-mint', 'Linux-Mint'), ('magento', 'Magento'), ('mariadb', 'Mariadb'), ('memcached', 'Memcached'), ('mongodb', 'Mongodb'), ('mysql', 'Mysql'), ('mysql-alt', 'Mysql-Alt'), ('netbsd', 'Netbsd'), ('nginx', 'Nginx'), ('nginx-alt', 'Nginx-Alt'), ('nodejs', 'Nodejs'), ('objectivec', 'Objectivec'), ('october', 'October'), ('opensource', 'Opensource'), ('osx', 'Osx'), ('perl', 'Perl'), ('phonegap', 'Phonegap'), ('photoshop', 'Photoshop'), ('php', 'Php'), ('php-alt', 'Php-Alt'), ('platter', 'Platter'), ('playframework', 'Playframework'), ('postcss', 'Postcss'), ('postgres', 'Postgres'), ('python', 'Python'), ('rails', 'Rails'), ('rails-alt', 'Rails-Alt'), ('rasbaerrypi', 'Rasbaerrypi'), ('react', 'React'), ('redhat', 'Redhat'), ('redis', 'Redis'), ('ruby', 'Ruby'), ('sass', 'Sass'), ('scala', 'Scala'), ('selenium', 'Selenium'), ('shell', 'Shell'), ('shell-alt', 'Shell-Alt'), ('shellscript', 'Shellscript'), ('solaris', 'Solaris'), ('sql', 'Sql'), ('sublime', 'Sublime'), ('suse', 'Suse'), ('svn', 'Svn'), ('tomcat', 'Tomcat'), ('ubuntu', 'Ubuntu'), ('visual-studio', 'Visual-Studio'), ('webpack', 'Webpack'), ('wordpress', 'Wordpress'), ('zend', 'Zend')], default='default', max_length=20)),
                ('custom_icon', models.CharField(blank=True, max_length=30)),
                ('skill_description', models.CharField(blank=True, max_length=200)),
                ('optional_class', models.CharField(blank=True, max_length=30)),
                ('placement', models.SmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='SkillGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
                ('skill_description', models.CharField(blank=True, max_length=250)),
                ('optional_icon', models.CharField(blank=True, max_length=30)),
                ('optional_class', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_group',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='homepage.SkillGroup'),
        ),
    ]
