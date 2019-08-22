<template>

            <div class="header">
                <div class="header_cont">
                    <div class="left">
                        <img src="https://hcdn1.luffycity.com/static/frontend/activity/head-logo_1564141048.3435316.svg"
                             alt="">
                        <nav class="nav">
                            <li v-for='(nav,i) in navlinks' :key="nav.id">
                                <span>
                                    <router-link :to='{name:nav.name}'>
                                        {{ nav.title }}
                                    </router-link>
                                </span>
                                <!--                                <span v-if="i === 2">New</span>-->
                            </li>
                        </nav>
                    </div>
                    <div class="header_right_box">
                        <!-- <el-dropdown> -->
                        <div class="nav-right" v-if='isLogin'>
                            <span class='el-dropdown-link'>学习中心</span>
                            <span class="user">老村长</span>
                            <img src="" alt="">
                            <ul class="my_account">
                                <li>
                                    我的账户
                                    <i>></i>
                                </li>
                                <li>
                                    我的订单
                                    <i>></i>
                                </li>
                                <li>
                                    我的优惠券
                                    <i>></i>
                                </li>
                                <li>
                                    我的消息<span class="msg">(44)</span>
                                    <i>></i>
                                </li>
                                <li>
                                    购物车<span class="count">(1)</span>
                                    <i>></i>
                                </li>
                                <li>
                                    退出
                                    <i>></i>
                                </li>
                            </ul>
                        </div>
                        <!-- </el-dropdown> -->
                        <div class="nav-right" v-else>
                            <span>登录</span>
                            &nbsp;| &nbsp;
                            <span>注册</span>
                        </div>
                    </div>
                </div>
            </div>



</template>

<script>
	export default {

		name: 'LuffyHeader',
		data() {
			return {
				isLogin: false,
				navlinks: [
					{id: 1, title: '首页', name: "Home"},
					{id: 2, title: '免费课程', name: "Course"},
					{id: 3, title: '轻课', name: "LightCourse"},
					{id: 4, title: '学位课程', name: "Micro"},
					{id: 5, title: '题库', name: "Title"},
					{id: 6, title: '学员成果', name: "Student"},

				]
			}
		}

	};
</script>

<style lang="css" scoped>
    .header {
        width: 100%;
        height: 80px;
        background: #fff;
        position: fixed;
        left: 0;
        top: 0;
        margin: 0 auto;
        display: -ms-flexbox;
        display: flex;
        z-index: 7;
        text-overflow: ellipsis;
        white-space: nowrap;
        box-shadow: 0 0.5px 0.5px 0 #c9c9c9;
    }

    .header_cont {
        width: 1200px;
        margin: 0 auto;
        line-height: 80px;

    }

    .header_cont img {
        vertical-align: middle;
        padding-top: 20px;
        float: left;
        margin-right: 50px;
    }

    .nav {
        width: 424px;
        height: 90%;
        font-size: 14px;
        color: #5e5e5e;
        display: -ms-flexbox;
        display: flex;
        line-height: 80px;
        cursor: pointer;
        position: relative;
        list-style: none;
        float: left;
    }

    .nav li {
        margin-right: 30px;
        color: #333333 ;
    }

    .nav li a {
        color: #333333;
    }

    /*.nav li span {*/
    /*    color: #4a4a4a;*/
    /*    width: 100%;*/
    /*    height: 60px;*/
    /*    display: inline-block;*/
    /*}*/

    /*.nav ul li a:hover{*/
    /*    color: #B3B3B3;*/
    /*}*/
    /*.nav ul li a.is-active{*/
    /*    color: #4a4a4a;*/
    /*    border-bottom: 4px solid #ffc210;*/
    /*}*/

    .header_right_box {
        float: right;
    }

    .nav-right {
        float: right;
        position: relative;
        z-index: 100;

    }

    .nav-right span {
        cursor: pointer;
    }

    .nav-right .user {
        margin-left: 15px;
    }

    .nav-right img {
        width: 26px;
        height: 26px;
        border-radius: 50%;
        display: inline-block;
        vertical-align: middle;
        margin-left: 15px;
    }

    .nav-right ul {
        position: absolute;
        width: 221px;
        z-index: 100;
        font-size: 12px;
        top: 80px;
        background: #fff;
        border-top: 2px solid #d0d0d0;
        box-shadow: 0 2px 4px 0 #e8e8e8;
    }

    .nav-right ul li {
        height: 40px;
        color: #4a4a4a;
        padding-left: 30px;
        padding-right: 20px;
        font-size: 12px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        cursor: pointer;
        transition: all .2s linear;
    }

    .nav-right ul li span.msg {
        margin-left: -80px;
        color: red;
    }

    .nav-right ul li span.count {
        margin-left: -100px;
        color: red;
    }
</style>
