spark python开发环境搭建



参考这个连接来安装好本地运行环境
http://ramhiser.com/2015/02/01/configuring-ipython-notebook-support-for-pyspark/
注意找网速比较好的环境安装

仔细阅读官方文档, 理解python接口的用法
http://spark.apache.org/docs/latest/quick-start.html

在pyshell环境下安装好以后, 可能会出现这个问题:

Error: Must specify a primary resource (JAR or Python or R file)

按照这个增加环境变量即可.
https://www.google.com.hk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0ahUKEwjh78Xx4KHKAhUGi5QKHUhnA7cQFggaMAA&url=http%3a%2f%2fstackoverflow.com%2fquestions%2f31193768%2ferror-must-specify-a-primary-resource-jar-or-python-or-r-file-ipython-noteb&usg=AFQjCNHpnVZJBUjxpp4CYNw8_TNKHhT-Ig&cad=rjt



总结:
 使用python接口来进行大数据的类map,reduce运算.
 本质是利用py4j把python的操作转换成java的操作执行集群计算.