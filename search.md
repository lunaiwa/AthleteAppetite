<html>
    <link rel="stylesheet" href="main.css">
    <link rel="stylesheet" href="index.css">
  <h1 style="padding-top: 3%;">What do you Want to Eat ?</h1>
  <br><br>
  <center>
  <h2> what ingredients do you have ? </h2>
  <form action="/recipes">
      <div class="input-group mb-3" style="max-width: 50%;">
          <input type="text" class="form-control" placeholder="INGREDIENT" aria-label="Ingredients" aria-describedby="button-addon2" name="ingredients">
          <div class="input-group-append">

<br>
<br>

<h2>what cusine ?</h2>

<select name="cusine" id="cars">
  <option value="asian">asain</option>
  <option value="greek">greek</option>
  <option value="italian">italian</option>

<br>
<br>

<h2>diet ?</h2>

<select name="diet" id="cars">
  <option value="vegetarian">asain</option>
  <option value="keto">greek</option>
  <option value="pescatarian">pescatarian</option>


<br>
<br>

<h2>meal type ?</h2>

<select name="mealtype" id="cars">
  <option value="breakfast">breakfast</option>
  <option value="lunch">lunch</option>
  <option value="dinner">dinner</option>

<br>
<br>

<h2>prep-time ?</h2>

<input type="text" class="form-control" placeholder="minutes" aria-label="minutes" aria-describedby="button-addon2" name="minuets"> 

<br>
<br>
<br>

<button class="btn btn-outline-secondary" type="submit" id="button-addon2">Search</button>

</select>


