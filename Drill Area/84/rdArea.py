#!/usr/bin/env python
# coding: utf-8

# In[38]:


import shapefile
sf = shapefile.Reader('范围(2014.10).shp')
Shapes = sf.shapes()


# In[39]:


import matplotlib.pyplot as plt
plt.figure()
for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x,y)
plt.show()


# In[34]:


import shapefile
sf2 = shapefile.Reader('钻孔1_Project.shp')
Shapes = sf2.shapes()


# In[28]:


for sr in sf2.shapeRecords():
    print(sr.shape.points[0])


# In[35]:


import matplotlib.pyplot as plt
listx=[]
listy=[]
for sr in sf2.shapeRecords():
    for xNew,yNew in sr.shape.points:
        listx.append(sr.shape.points[0])
plt.scatter([x[0] for x in listx], [x[1] for x in listx], c = 'k', s = 2, marker='o')
plt.show()

