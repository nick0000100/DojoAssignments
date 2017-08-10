INSERT INTO users (id, first_name, last_name, created_at, updated_at)
VALUES (1, "Jo", "Lo", NOW(), NOW());

INSERT INTO users (id, first_name, last_name, created_at, updated_at)
VALUES (2, "Mo", "Lo", NOW(), NOW());

INSERT INTO users (id, first_name, last_name, created_at, updated_at)
VALUES (3, "Ko", "Po", NOW(), NOW());

INSERT INTO users (id, first_name, last_name, created_at, updated_at)
VALUES (4, "Wo", "No", NOW(), NOW());

INSERT INTO users (id, first_name, last_name, created_at, updated_at)
VALUES (5, "Co", "Xo", NOW(), NOW());

INSERT INTO friendships (id, user_id, friend_id, created_at, updated_at)
VALUES (1, 1, 2, NOW(), NOW());

INSERT INTO friendships (id, user_id, friend_id, created_at, updated_at)
VALUES (2, 2, 1, NOW(), NOW());

INSERT INTO friendships (id, user_id, friend_id, created_at, updated_at)
VALUES (3, 2, 4, NOW(), NOW());

INSERT INTO friendships (id, user_id, friend_id, created_at, updated_at)
VALUES (4, 4, 2, NOW(), NOW());

INSERT INTO friendships (id, user_id, friend_id, created_at, updated_at)
VALUES (5, 5, 1, NOW(), NOW());

INSERT INTO friendships (id, user_id, friend_id, created_at, updated_at)
VALUES (6, 1, 5, NOW(), NOW());