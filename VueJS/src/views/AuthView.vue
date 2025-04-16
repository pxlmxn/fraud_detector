<script>

</script>

<template>

<main class="form-signin w-100 m-auto">
  <form>
    
    <h1 class="h3 mb-3 text-center fw-normal">Авторизация</h1>

    <div class="form-floating">
      <input type="text" class="form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">Введите логин</label>
    </div>
    <div class="form-floating">
      <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
      <label for="floatingPassword">Введите пароль</label>
    </div>
    <div class="form-check text-start my-3">
      <input class="form-check-input" type="checkbox" value="remember-me" id="checkDefault">
      <label class="form-check-label" for="checkDefault">
        Запомнить меня
      </label>
    </div>

    <div class="text-center">
    <button class="btn btn-primary text-center w-25 py-2" type="submit">Войти</button>
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
  .form-check{
    padding-left: 26.5%;
  }
  
  
</style>