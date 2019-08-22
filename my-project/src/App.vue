<template>
    <div id="app">
        <div class="container">
            <LuffyHeader/>
        </div>
        <router-view/>
    </div>
</template>

<script>
	export default {
		name: 'App',
		data() {
			return {}
		},
	}
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        /*text-align: center;*/
        margin-top: 60px;
        background-color: #f6f6f6;
    }

    /*li {*/
    /*    list-style: none;*/
    /*    float: left;*/
    /*    margin-left: 20px;*/
    /*}*/
</style>
