<script>
import axios from "axios";
export default {
    data() {
		return {
			complaint: {}
		};
	},
    mounted() {
        this.loadComplaint();
    },
    methods: {
        async loadComplaint() {
            let response = await axios.get('http://127.0.0.1:8000/complaint');
            this.complaint = response.data;
        },
    },
}
</script>
<template>

</template>
<style scoped>

</style>