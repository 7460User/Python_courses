def display(**kvr):
    
  print("Number of Varible of lenght Value={}".format(len(kvr)))
  for k,v in kvr.items():
    print("{}---->{}".format(k,v))

display(sno="1",sname="Rama",crs="pyrhon")
display(sno="2",sname="sonu",crs="java")
display(sno="3",sname="Reeta",crs="UI Developer")
display(sno="4",sname="vanadani",crs="Angular")
display(sno="5",sname="chandani",crs="Api")