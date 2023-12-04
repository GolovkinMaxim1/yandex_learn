-- Создание фильмов
create table if not exists content.film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    rating FLOAT,
    type TEXT not null,
    created timestamp with time zone,
    modified timestamp with time zone
);

create index film_work_creation_date_index
    on content.film_work (creation_date);
create index film_work_rating_index
    on content.film_work (rating);


-- Создание жанров
create table if not exists content.genre
(
    name        text unique not null,
    description text,
    created timestamp with time zone,
    modified timestamp with time zone,
    id          uuid primary key
);
create index genre_name_index
    on content.genre (name);

create table if not exists content.person
(
    id        uuid not null
        primary key,
    full_name text not null,
    created   timestamp with time zone,
    modified  timestamp with time zone

);
create index person_full_name_index
    on content.person (full_name);

create table if not exists content.genre_film_work
(
    id           uuid not null
        primary key,
    genre_id     uuid not null
        constraint genre_film_work_film_work_id_fk
            references content.film_work,
    film_work_id uuid not null
        constraint genre_film_work_film_work_id_fk2
            references content.film_work,
    created      timestamp with time zone

);
create index genre_film_work_genre_id_index
    on content.genre_film_work (genre_id);
create index genre_film_work_film_work_id_index
    on content.genre_film_work (film_work_id);

create table if not exists content.person_film_work
(
    person_id    uuid                     not null
        constraint person_film_work_person_id_fk
            references content.person,
    film_work_id uuid                     not null
        constraint person_film_work_film_work_id_fk
            references content.film_work,
    role         text                     not null,
    created      timestamp with time zone not null
);
create index person_film_work_person_id_index
    on content.person_film_work (person_id);
create index person_film_work_film_work_id_index
    on content.person_film_work (film_work_id);
