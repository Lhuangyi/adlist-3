import csv  # https://docs.python.org/3/library/csv.html

# python3 manage.py shell < many/load.py

from unesco.models import Site, Category, States, Iso, Region

Site.objects.all().delete()
Category.objects.all().delete()
States.objects.all().delete()
Iso.objects.all().delete()
Region.objects.all().delete()

fh = open('unesco/whc-sites-2018-small.csv')
reader = csv.reader(fh)

for row in reader:
    if row[0] == 'name':
        print("This title row")
    else:
        try:
            c = Category.objects.get(name=row[7])
        except:
            print("Inserting category",row[7])
            c = Category(name=row[7])
            c.save()


        try:
            i = Iso.objects.get(name=row[10])
        except:
            print("Inserting iso",row[10])
            i = Iso(name=row[10])
            i.save()


        try:
            r = Region.objects.get(name=row[9])
        except:
            print("Inserting region",row[9])
            r = Region(name=row[9])
            r.save()


        try:
            st = States.objects.get(name=row[8])
        except:
            print("Inserting states",row[8])
            st = States(name=row[8])
            st.save()

        try:
            y=int(row[3])
        except:
            y=None

        try:
            area=float(row[6])
        except:
            area=None

        print("Inserting site",row[0])
        si = Site(name=row[0],description=row[1],justification=row[2],
        year=y,longitude=row[4],latitude=row[5],area_hectares=area,
        category=c,states=st,iso=i,region=r)
        si.save()


'''

    try:
        c = Category.objects.get(name=row[7])
    except:
        print("Inserting category",row[7])
        c = Category(name=row[7])
        c.save()


    try:
        i = Iso.objects.get(name=row[10])
    except:
        print("Inserting iso",row[10])
        i = Iso(name=row[10])
        i.save()


    try:
        r = Region.objects.get(name=row[9])
    except:
        print("Inserting region",row[9])
        r = Region(name=row[9])
        r.save()


    try:
        st = States.objects.get(name=row[8])
    except:
        print("Inserting states",row[8])
        st = States(name=row[8])
        st.save()



    print("Inserting site",row[0])
    si = Site(name=row[0],description=row[1],justification=row[2],
    year=row[3],longitude=row[4],latitude=row[5],area_hectares=row[6],
    category=c,states=st,iso=i,region=r)
    si.save()
    '''
