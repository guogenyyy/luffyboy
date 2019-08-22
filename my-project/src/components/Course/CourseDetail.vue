<template>
    <div class="wrap">
        <div class="head-wrap">
            <div class="head-video">
                <div class="videos">
                    <div class="img">
                    </div>
                </div>
                <div class="item">
                    <p class="name">{{ course.name }}</p>
                    <p class="data">260人在学 &nbsp;&nbsp;&nbsp;&nbsp;课程总时长：&nbsp;&nbsp;&nbsp;&nbsp;</p>
                    <div class="preferential">限时折扣</div>
                    <p class="price bac">价格：{{course.price}}</p>
                    <div class="bottom">
                        <p>
                            <el-button type="primary" plain>立即购买</el-button>
                            <el-button type="success" plain>免费试学</el-button>
                        </p>
                        <p>
                            <el-button id="addshopping" type="info" plain>加入购物车</el-button>
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div class="tab">
            <ul>
                <li>详情介绍</li>
                <li>课程章节</li>
                <li>用户评论</li>
                <li>常见问题</li>
            </ul>
        </div>
        <div class="item">
            12313545
        </div>
    </div>
</template>

<script>
	export default {

		name: 'CourseDetail',
		data() {
			return {
				course: [],
			}
		},
		methods: {

			//获取课程详情  包含 价格套餐
			getCourseDetail() {
				let course_id = this.$route.params.courseId
				this.$http.courseDetail(course_id)
					.then(res => {
						console.log(res)
						this.course = res.data
					})
					.catch(err => {
						console.log(err);
					})
			}
		},
		created() {
			this.getCourseDetail()
		}
	};
</script>

<style lang="css" scoped>
    .wrap {
        width: 100%;
    }

    .head-wrap {
        width: 100%;
        height: 388px;
        padding-top: 30px;
        background-color: #fff;
    }

    .head-video {
        width: 1200px;
        height: 100%;
        margin: 0 auto;

    }

    .videos {
        width: 690px;
        height: 100%;
        float: left;
    }

    .videos .img {
        height: 100%;
        background-image: url("../../../static/images/9A12C43204184069958FEFA9DB03A0A5-6-2.png");
        background-repeat: no-repeat;
        background-size: 100%;
        margin-left: 0px;
        margin-top: 0px;
    }

    .head-video .item {
        width: 510px;
        height: 100%;
        float: left;
        position: relative;
    }

    .tab {
        height: 68px;
        margin-bottom: 30px;
        background-color: #fff;
    }

    .tab ul {
        width: 1200px;
        height: 100%;
        margin: 0 auto;
    }

    .tab li {
        font-size: 17px;
        margin-right: 15px;
        padding: 26px 20px 16px;
        float: left;
    }

    .item .name {
        font-size: 20px;
        width: 464px;
        height: 28px;
        padding: 10px 23px;
    }

    .item .data {
        height: 20px;
        font-size: 14px;
        color: #9B9B9B;
        padding: 0 23px 16px;
    }

    .preferential {
        height: 32px;
        line-height: 32px;
        color: #fff;
        padding: 10px 23px;
        background-color: #fa6240;
    }

    .price {
        height: 32px;
        line-height: 1.5;
        padding: 5px 23px;
    }

    .bottom {
        padding: 0 23px;
        position: absolute;
        bottom: 20px;
    }

    .bottom p {
        display: inline-block;
    }

    #addshopping {
        margin-left: 100px;
    }

    .item {
        height: 120px;
    }


</style>
