INSERT INTO Books (title, author, price, publisher)
VALUES
    ('Decouple Django', 'Gagliardi', 3874, 'APress'),
    ('Beginning Django', 'Rubio', 3053, 'APress'),
    ('Pro Django', 'Alchin', 4284, 'APress');

-- Verify inserted records
SELECT * FROM Books;

-- Retrieve  books in alphabetical order
SELECT * FROM Books
ORDER BY title ASC;