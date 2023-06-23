var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    quotesData = JSON.parse(this.responseText);
    document.getElementById("text").innerHTML = quotesData.quotes[0].quote;
    document.getElementById("author").innerHTML = quotesData.quotes[0].author;
  }
};
xhttp.open("GET", "https://gist.githubusercontent.com/camperbot/5a022b72e96c4c9585c32bf6a75f62d9/raw/e3c6895ce42069f0ee7e991229064f167fe8ccdc/quotes.json", true);
xhttp.send();

function getQuote() {
  console.log("getQuote:");
  let randomQuote = quotesData.quotes[Math.floor(Math.random() * quotesData.quotes.length)];
  document.getElementById("text").innerHTML = randomQuote.quote;
  document.getElementById("author").innerHTML = randomQuote.author;
}