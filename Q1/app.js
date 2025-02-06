function displayDate() {
    const today = new Date();

    const formattedDate = today.toLocaleDateString('en-US', {
      weekday: 'long', 
      year: 'numeric', 
      month: 'long', 
      day: 'numeric' 
    });

    document.getElementById("date").textContent = formattedDate;
  }
  window.onload = displayDate;

function adding() {
    let num1 = parseFloat(document.getElementById("num").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    document.getElementById("res").textContent = num1+num2;
}

function sub() {
    let num1 = parseFloat(document.getElementById("num").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    document.getElementById("res").textContent = num1 - num2;
}

