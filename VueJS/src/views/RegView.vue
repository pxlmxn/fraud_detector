<script>

</script>

<template>

<main class="form-signin w-100 m-auto">
  <form>
    
    <h1 class="h3 mb-3 text-center fw-normal">Регистрация</h1>

    <div class="form-floating">
      <input type="text" class="form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">Придумайте логин</label>
    </div>
    <div class="form-floating">
      <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
      <label for="floatingPassword">Придумайте пароль</label>
    </div>
    <div class="form-floating">
      <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
      <label for="floatingPassword">Повторите пароль</label>
    </div>

    <div class="text-center">
    <button class="btn btn-primary text-center w-25 py-2" type="submit">Зарегистрироваться</button>
    </div>
  </form>
</main>
</template> 
<style>
  .form-floating{
    width: 50%;
    margin: 0 auto;
    margin-bottom: 30px;
  }
  button{
    width: 140px;
    margin: 0 auto;
    margin-bottom: 30px;
  }
  
  
</style>