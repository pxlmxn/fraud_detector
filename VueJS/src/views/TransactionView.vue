<script>
import axios from "axios";
export default {
    data() {
		return {
			txn: {}
		};
	},
    mounted() {
        this.loadTxn();
    },
    methods: {
        async loadTxn() {
            let response = await axios.get('http://127.0.0.1:8000/txn');
            this.txn = response.data;
        },
    },
}
</script>

<template>

</template>

<style scope>

</style>
