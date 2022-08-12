let modal = document.getElementById("myModal");

  // Get the button that opens the modal
  let btn = document.getElementById("asd1234");

  // Get the <span> element that closes the modal
  let span = document.getElementsByClassName("close")[0];
  let iframeButton = document.getElementById("modal-button-iframe");
  iframeButton.onclick = function () {
    alert("user want to add Iframe")
  }
  // When the user clicks the button, open the modal 
  btn.onclick = function () {
    modal.style.display = "block";
  }

  // When the user clicks on <span> (x), close the modal
  span.onclick = function () {
    modal.style.display = "none";
  }

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
  function alertme(){
    alert('hello ');
  }