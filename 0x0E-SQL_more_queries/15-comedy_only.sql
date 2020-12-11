-- Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
SELECT tv_shows.title FROM tv_shows
-- aqui relaciono el tabla show que contine el title de la serie con la que mezcal a las dos
JOIN  tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- aqui relaicono el tv_genres name con el title a que pertenece 
-- osea tomo tl title que se relaciona en etse caso con un genero de comedia
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY  tv_shows.title;
