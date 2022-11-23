def test_create_imovel(client):
    author = Author.objects.create(name='Luciano Ramalho')
    data = {
        "name": 'Python fluente',
        "edition": 2,
        "publication_year": 2022,
        "authors": [author.id]
    }
    response = client.post('/api/books/', data=data, content_type=CT_JSON)

    assert response.status_code == HTTPStatus.CREATED
    book = Book.objects.first()
    assert response['Location'] == f'/api/books/{book.id}/'
    assert book is not None

    response_data = response.json()
    assert response_data['name'] == 'Python fluente'
    assert response_data['edition'] == 2
    assert response_data['publication_year'] == 2022
    assert response_data['authors'] == [author.id]
    assert response_data['id'] == book.id