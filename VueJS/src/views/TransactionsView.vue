<script>
import axios from "axios";
export default {
    data() {
		return {
			txns: []
		};
	},
    mounted() {
        this.loadTxns();
    },
    methods: {
        async loadTxns() {
            let response = await axios.get('http://127.0.0.1:8000/txns');
            this.txns = response.data;
        },
    },
}
</script>

<template>
  <main>
    
  </main>
</template>
