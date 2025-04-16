<script>
import axios from "axios";
export default {
    data() {
		return {
			data: {}
		};
	},
    mounted() {
        this.loadData();
    },
    methods: {
        async loadData() {
            let response = await axios.get('http://127.0.0.1:8000/dashboard');
            this.data = response.data;
        },
    },
}
</script>
<template>

</template>
<style scope>

</style>