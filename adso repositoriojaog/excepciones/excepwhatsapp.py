blog_posts = [{'Photos': 3, 'Megusta': 21, 'comentarios': 2}, {'Megusta': 13, 'comentarios': 2, 'compartido': 1}, {'Photos': 5, 'Megusta': 33, 'comentarios': 8, 'compartido': 3}, {'comentarios': 4, 'compartido': 2}, {'Photos': 8, 'comentarios': 1, 'compartido': 1}, {'Photos': 3, 'Megusta': 19, 'comentarios': 3}]

total_Megusta = 0
vcs=0
try:
    for post in blog_posts:
        vcs+=1
        total_Megusta+=post['Megusta']
        print('por el momento hay=',total_Megusta,'Megusta')
except KeyError:
    print('¡¡en la publicacion numero',vcs,'no encontramos Megusta y paramos la busqueda!!')