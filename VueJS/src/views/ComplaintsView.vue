<script>
import axios from "axios";
export default {
    data() {
		return {
			complaints: []
		};
	},
    mounted() {
        this.loadComplaints();
    },
    methods: {
        async loadComplaints() {
            let response = await axios.get('http://127.0.0.1:8000/complaints');
            this.complaints = response.data;
        },
    },
}
</script>
<template>

</template>
<style scoped>

</style>