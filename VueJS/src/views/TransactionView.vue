



<template>

<div class="css-grid-table">

<div class="css-grid-table-header">
<div>Дата.Время</div>
<div>Отправитель</div>
<div>Получатель</div>
<div>Сумма перевода</div>
</div>

<div class="css-grid-table-body">
<div>n</div>
<div>n</div>
<div>n</div>
<div>n</div>
<div><button>delete</button></div>
<div><button>confirm</button></div>


</div>
</div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
.css-grid-table,
.css-grid-table-header,
.css-grid-table-body {
display: grid;
}

.css-grid-table {
grid-template-rows: 24px 72px;
width: 100%;
}

.css-grid-table-header,
.css-grid-table-body {
grid-template-columns: 20% 20% 20% 20% 10% 10%;
width: 100%;
line-height: 24px; 
}

.css-grid-table-header {
grid-column-gap: 2px;
grid-template-rows: auto;
}

.css-grid-table-body {
grid-template-rows: auto auto auto;
}

.css-grid-table-header div {
text-align: center;
font-weight: bold;
background-color: rgb(191, 191, 191);
}

.css-grid-table-body div {
padding-left: 6px;
}

</style>
