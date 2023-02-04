<template>
    <main role="main" class="col-12 p-4 main-section">
    <div class="container">
        <div class="row">
            <div class="col-6">
                <table class="table table-bordered">
                            <thead>
                                <tr>
                                    <th scope="col">#</th>
                                    <th scope="col">APIKEY</th>
                                    <th scope="col">Create Date</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <th scope="row">1</th>
                                    <td>Mark</td>
                                    <td>Mark</td>
                                </tr>
                                <tr>
                                    <th scope="row">2</th>
                                    <td>Jacob</td>
                                    <td>Mark</td>
                                </tr>
                                <tr>
                                    <th scope="row">3</th>
                                    <td >Larry the Bird</td>
                                    <td>Mark</td>
                                </tr>
                            </tbody>
                            </table>
            </div>
            <div class="col-6">
                <button class="btn btn-success">
                            <i class="bi bi-plus"></i>
                            Create new APIKey
                        </button>
            </div>
        </div>
    </div>
  </main>
</template>

<script>
    export default {
        
    }
</script>

<style  scoped>
.main-section {
  width: 80%;
}

</style>