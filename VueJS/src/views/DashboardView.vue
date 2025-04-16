<template>
<main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
      <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
        <h1 class="h2">Dashboard</h1>
        <div class="btn-toolbar mb-2 mb-md-0 buttons">
          <button type="button" class="btn btn-sm btn-outline-secondary dropdown-toggle d-flex align-items-center gap-1">
            <svg class="bi" aria-hidden="true"><use xlink:href="#calendar3"></use></svg>
            Эта неделя
          </button>
        </div>
      </div>

      <canvas class="my-4 w-100" id="myChart" width="100%" height="" style="display: block; box-sizing: border-box; height: 440px; width: 1042px;"></canvas>

      <h2>Заголовок секции</h2>
      <div class="table-responsive small">
        <table class="table table-striped table-sm">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Header</th>
              <th scope="col">Header</th>
              <th scope="col">Header</th>
              <th scope="col">Header</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>n</td>
              <td>n</td>
              <td>n</td>
              <td>n</td>
              <td>n</td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>

</template>
<style>
    .buttons button{
        height: 100px;
    }

</style>