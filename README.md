# DjangoLog
A weblog app for learning django

# 课程目标  

一天学会使用Django写网站

# 课程目录 

| 阶段 | 课程 |
| --- | --- |
| 第一章 效果演示 | <ol><li><div>DjangoLog效果演示</div><div>DjangoLog项目实现了写文章、文章编辑器、文章列表、文章详情、用户管理等功能</div></li></ol> |
| 第二章 环境搭建 | <ol><li>安装数据库<div>为了方便对数据库进行管理，在安装MySQL的同时我们通常会再安装MySQL的管理工具，而这个过程相对复杂，所以我们选择直接安装XAMPP这个集成的运行环境，它包括Apache、PHP、MySQL和PHPMyAdmin，一键安装，大大提升了效率。</div></li><li>开发Python程序<div>PyCharm是由JetBrains开发的一个Python语言的集成开发环境，非常智能，能够大大提高开发效率。由于Django推荐我们使用Python3，所以在本套课程中我们演示的是如何安装Python3。</div></li></ol>
| 第三章 开发DjangoLog项目 | <ol><li>创建Django项目<div>演示在Windows平台及Mac平台如何使用命令行创建项目，并演示如何使用PyCharm创建项目。</div></li><li>创建blog应用<div>可以通过manage.py创建和管理应用。</div></li><li>使用模板技术<div>Django模板技术非常强大，可以很方便的从view层传递参数给模板，而且模板还支持继承，所声明的block代码块可以被子模板重写。</div></li><li>连接和使用MySQL数据库<div>使用manage.py可以自动生成数据库结构及相关数据，创建的超级用户可以直接用于登陆Django的admin页面。PyCharm自带的数据库管理工具使用起来也非常方便。</div></li><li>配置网站主框架<div>Django对于静态文件的支持也非常强大，默认情况下，在debug=True的模式下，使用Django内置的静态文件服务器来支持静态文件，直接将文件放在my_app/static/my_app目录下即可，如将a.html文件放置为该目录，然后通过 http://127.0.0.1/static/my_app/a.html 访问，也可以自定义静态文件目录，在本课中所演示的方式就是自定义静态文件目录。在生产环境下应该设置debug=False，使用Apache、Nginx等类似的服务器支持静态文件。</div></li><li>声明文章模型<div>直接声明一个模型，便可以直接使用该模型生成数据库结构，非常强大。</div></li><li>使用编辑器<div>textarea只能用于编辑简单的字符串，如果想编辑复杂的HTML代码，那需要使用编辑器，在这里我们推荐使用ckeditor</div></li><li>呈现文章列表<div>使用Django自带的ListView可以快速生成文章列表信息。</div></li><li>实现文章页面<div>Django拥有强大的自定义url规则的能力，配置DetailView可以快速生成详情页面。</div></li></ol> |

