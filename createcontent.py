import sqlite3


def create_user(id, idblock, short_title, img, altimg, title, contenttext, author, timestampdata):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO content (id, idblock, short_title, img, altimg, title, contenttext, author, timestampdata) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (id, idblock, short_title, img, altimg, title, contenttext, author, timestampdata))
    conn.commit()
    conn.close()



create_user(1, 'carouselExampleIndicators', 'Slider', 'https://via.placeholder.com/1024x500', 'image 1', 'Title Test 1', 'some text for slider 1', None, None);
create_user(2, 'carouselExampleIndicators', 'Slider', 'https://via.placeholder.com/1024x500', 'image 2', 'Title Test 2', 'some text for slider 2', None, None);
create_user(3, 'cards', 'miniCards', 'https://via.placeholder.com/150', 'mini img 2', 'mini card 2', 'text for mini card 2', None, None);
create_user(4, 'cards', 'miniCards', 'https://via.placeholder.com/150', 'mini img 1', 'mini card 1', 'text for mini card 1 ', None, None);