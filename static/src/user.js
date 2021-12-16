// Front end functions for user GUI and event handlers

function pinClickHandler(e){
    const element = e.currentTarget;
    const card = document.getElementById("card");
    const drop = document.getElementById("drop");

    const id = document.getElementById("issue-id");
    const description = document.getElementById("issue-description");
    const category = document.getElementById("issue-category");
    const score = document.getElementById("score");
    const downvotes = document.getElementById("downvote");
    const upvotes = document.getElementById("upvote");
    

    card.style.display = "flex";
    drop.style.pointerEvents = "auto";

    drop.addEventListener("click",  () => {
      card.style.display = "none"
      drop.style.pointerEvents = "none";
    })

    id.innerHTML = "Issue #" + element.getAttribute("data-id");
    description.innerHTML = element.getAttribute("data-description");
    category.innerHTML = element.getAttribute("data-category");
    score.innerHTML = element.getAttribute("data-score");
    // downvotes.innerHTML = element.getAttribute("data-downvotes");
    // upvotes.innerHTML = element.getAttribute("data-upvotes");
    
  }

  function menuClickHandler(e){
    const menuScreen = document.getElementById("menu-screen");
    const drop = document.getElementById("drop");
    const menu = document.getElementById("menu");

    menuScreen.style.display = "flex";
    menu.style.display = "none";
    drop.style.pointerEvents = "auto";

    drop.addEventListener("click",  () => {
      menuScreen.style.display = "none"
      drop.style.pointerEvents = "none";
      menu.style.display = "inline";
    })
  }

  function newIssueHandler(e){
  
    const coordinates = e.lngLat;
    const drop = document.getElementById("drop");
    const issue = document.getElementById("new-issue");

    issue.style.display = "flex";
    drop.style.pointerEvents = "auto";

    drop.addEventListener("click",  () => {
      issue.style.display = "none"
      drop.style.pointerEvents = "none";
    })
  }

  function init(){
    const menu = document.getElementById("menu");
    menu.addEventListener("click", menuClickHandler)
}