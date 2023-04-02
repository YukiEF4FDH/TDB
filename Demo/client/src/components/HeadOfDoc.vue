<template>
  <!DOCTYPE html>
  <header>
    <p class="header-timestamp">Double click to edit the Date</p>
    <hr />
    <div class="header-owner">
      <img class="header-owner-icon" src="https://gyazo.com/c9557c094a1490cf9ebad4163112810d.png" />
      <p class="header-owner-info">
        <img src="https://gyazo.com/79043abe41dda65e42fff7d3f5b8ab5b.png" />
        <br />
        <b>Double click</b><br />
        To edit the info here<br />
        <small>TEL: xxxxxxx</small><br />
        <small>URL: xxx</small><br />
        <small>xxxxxxxx</small><br />
      </p>
    </div>
    <div class="header-outline">
      <div class="outline" @dblclick="dbClickOutline($event)">Double Click to Edit the Outline</div>
    </div>
    <h1 class="header-title" @dblclick="dbClickTitle($event)">
      Double Click to Edit the Title
    </h1>
    <h2 class="header-title" @dblclick="dbClickTitle2($event)">
      ~ Double Click to Edit the Subtitle ~
    </h2>
  </header>
</template>



<script>
import { render } from 'vue'
let isInputTitle = false

export default {
  name: "HeadOfDoc",
  methods: {
    dbClickOutline(e) {
      let target = e.currentTarget
      let parent = target.parentElement
      console.log(target)
      console.log(parent)
      let newInput = document.createElement("input")
      newInput.setAttribute("type", "text")
      newInput.setAttribute("id", "newInputId1")
      parent.appendChild(newInput)
      console.log(newInput)
      console.log(parent)
      target.remove()
      isInputTitle = true

      let mystyle="  font-weight: bold; font-size: 20px; text-align: center; border: 2px solid black; padding: 1%; width:fit-content; display: flex; justify-content: center;"

      document.addEventListener('click', function (event) {
        if (isInputTitle&&(event.target.id!="newInputId1")) {
          let newOutline = document.getElementById("newInputId1").value
          let newOutlineVNode = <div class="outline" style={mystyle}>{newOutline}</div>
          let el = document.createElement("div")
          render(newOutlineVNode, el)
          let newNode = el.childNodes[0]

          newInput.remove()
          parent.appendChild(newNode)
          isInputTitle = false
        }
      });

    },
    dbClickTitle(e){
      let target = e.currentTarget
      let newInput = document.createElement("input")
      newInput.setAttribute("type", "text")
      newInput.setAttribute("id", "newInputId2")
      target.innerText = ""
      target.appendChild(newInput)
      isInputTitle = true

      document.addEventListener('click', function (event) {
        if (isInputTitle&&(event.target.id!="newInputId2")) {
          let newOutline = document.getElementById("newInputId2").value
          newInput.remove()
          target.innerText = newOutline
          isInputTitle = false
        }
      });
    },
    dbClickTitle2(e){
      let target = e.currentTarget
      let newInput = document.createElement("input")
      newInput.setAttribute("type", "text")
      newInput.setAttribute("id", "newInputId3")
      target.innerText = ""
      target.appendChild(newInput)
      isInputTitle = true

      document.addEventListener('click', function (event) {
        if (isInputTitle&&(event.target.id!="newInputId3")) {
          let newOutline = document.getElementById("newInputId3").value
          newInput.remove()
          target.innerText = newOutline
          isInputTitle = false
        }
      });
    },
  }
};

</script>

<style scoped>
header {
  margin-left: 5%;
  margin-right: 5%;
  margin-bottom: 5%;
}

.header-timestamp {
  margin: 0px;
  text-align: right;
  font-size: 20px;
}

hr {
  *margin: 0;
  color: #000000;
  background-color: #000000;
  height: 1px;
}

.header-owner {
  height: 140px;
  margin: 0px;
  margin-bottom: 1%;
}

.header-owner-icon {
  text-align: left;
  width: 100px;
  height: 40px;
}

.header-owner-info {
  margin-top: 0px;
  float: right;
  text-align: right;
}

a {
  color: #000000;
}

.header-outline {
  margin-top: 1%;
  margin-bottom: 5%;
  text-align: center;
  display: flex;
  justify-content: center;
}

.outline {
  font-weight: bold;
  font-size: 20px;
  text-align: center;
  border: 2px solid black;
  padding: 1%;
  width:fit-content;
  display: flex;
  justify-content: center;
}

.header-title {
  text-align: center;
  display: flex;
  justify-content: center;
}

h1 {
  font-size: 27px;
  margin-bottom: 1%;
}

h2 {
  margin-top: 0%;
  font-size: 22px;
  font-weight: 500;
  margin-bottom: 3%;
}
</style>
