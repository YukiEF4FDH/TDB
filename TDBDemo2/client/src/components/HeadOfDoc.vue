<template>
  <header class="header">
    <p class="header-timestamp">2020/12/22</p>
    <hr class="header-hr" />
    <div class="header-owner">
      <img class="header-owner-icon"  src="https://gyazo.com/c9557c094a1490cf9ebad4163112810d.png"/>
      <p class="header-owner-info">
        <img src="https://gyazo.com/79043abe41dda65e42fff7d3f5b8ab5b.png"/>
		<br/>
        <b>横浜支店</b><br/>
        横浜市中区弁天通4-51<br/>
        <small>TEL: 045-641-0380</small><br/>
        <small>URL: <a href="https://www.tdb.co.jp">https://www.tdb.co.jp</a></small><br/>
        <small>景気動向オンライン <a href="https://www.tdb-di.com">https://www.tdb-di.com</a></small><br/>
      </p>
    </div>
    <div class="header-outline">
      <outline>特別企画: 2021 年の景気見通しに対する神奈川県内企業の意識調査</outline>
    </div>
    <h1 class="header-title">
      2021 年景気、県内企業の3 割が悪化見込み
    </h1>
    <h2 class="header-title">
      ～ 景気回復に必要な施策、「感染症の収束」が6 割超 ～
    </h2>
  </header>
</template>

<script>
	export default {
		name: "HeadOfDoc",
	};
</script>

<style>
.header{
  margin-left: 5%;
  margin-right: 5%;
}

a {
	color: #000000;
}

.header-timestamp {
  margin: 0px;
  text-align: right;
  font-size: 20px;
}

.header-hr {
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

.header-outline {
  margin-top: 1%;
  margin-bottom: 5%;
  text-align: center;
}

outline {
  margin: 10%;
  font-weight: bold;
  font-size: 20px;
  text-align: center;
  border: 2px solid black;
  margin: auto;
  padding: 1%;
}

.header-title {
  text-align: center;
}

h1 {
  font-size: 27px;
  margin-bottom: 1%;
}

h2 {
  margin-top: 0%;
  font-size: 22px;
  font-weight: 500;
}
</style>
