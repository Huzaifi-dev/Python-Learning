#  call sub module this way when init is empty 
from Foldermodule import circle   # 1st way: circle is the file name inside a folder
from Foldermodule.circle import area   # 2nd way: another way we called a fun name 

#  there is a another way we can setup init file and then import
# -------------------------------------------------


#  1st way
print(circle.area(5))


# 2nd way : we directly write fun name
print(area(5))