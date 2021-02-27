const fetchBooks = async () => {
    const result = await fetch("/api/bundle");
    return await result.json();
}

fetchBooks().then(books => {
    const bookOptions = document.getElementById("book-options")
    books.forEach(book => {
        console.log(book)
    })
}).catch(error=>console.log(error))