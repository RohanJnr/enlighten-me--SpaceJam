const booksTabBtn = document.getElementById("books-tab")
const OffersTabBtn = document.getElementById("offers-tab")
const TradesTabBtn = document.getElementById("trades-tab")

const btns = [booksTabBtn, OffersTabBtn, TradesTabBtn]

btns.forEach(btn => {
    btn.addEventListener("click", e => {
        const target = e.target
        const visible = target.getAttribute("data-visible")
        const inVisible = target.getAttribute("data-invisible").split(",")

        document.querySelectorAll(`.${visible}`).forEach(element => element.style.display = "flex")
        inVisible.forEach(item => {
            document.querySelectorAll(`.${item}`).forEach(element => element.style.display = "none")
        })
    })
})