<template>
    <div class="el-main">
        <div class="main">
            <div class="screening">
                <div class="ul1">
                    <p>课程分类：</p>
                    <ul>
                        <!-- v-for --start   -->
                        <li @click="categoryHandler(index,item.id)" v-for="(item,index) in categoryList" :key="item.id"
                            :class="{active:index==currentIndex}">{{item.name}}
                        </li>
                    </ul>
                </div>
            </div>
            <div class="course-list left">
                <!-- 课程列表   -->
                <dl @click="courseHandler(course.id)" v-for="(course) in courseList" :key="course.id">
                    <dt>
                        <img :src='course.course_img'
                             alt="">
                    </dt>
                    <dd>
                        <p>{{course.name}}</p>
                        <p>{{course.learn_number}} 已加入学习</p>
                        <div class="teacher">
                            <p>{{course.teacher_description}}</p>
                            <p>共 {{course.numbers}} 课时</p>
                        </div>
                        <ul>

                        </ul>
                        <div class="price">
                            <!--                            <span>{{item.promotion_name}}</span>-->
                            <!--                            <span>{{item.promotion_price}}</span>-->
                            <!--                            <span>{{item.price}}</span>-->
                            <button>立即购买</button>
                        </div>
                    </dd>
                </dl>
            </div>
        </div>
    </div>
</template>

<script>
	export default {
		name: "Course",
		data() {
			return {
				categoryList: [], //分类列表
				currentIndex: 0,
				courseList: [],  //课程列表
				categoryId: 0,
			}
		},
		methods: {
			// 获取分类列表
			getCategoryList() {
				this.$http.categoryList()
					.then((res) => {
						// console.log(res);
						if (res.error_no === 0) {
							this.categoryList = res.data;
							let obj = {
								id: 0,
								name: '全部',
								category: 0
							};
							this.categoryList.unshift(obj);
							//数组删除任意一个指定元素
						}
					})
					.catch((err) => {
						console.log('获取失败！')
					})
			},
			categoryHandler(index, categoryId) {

				this.currentIndex = index;
				this.categoryId = categoryId;
				console.log(this.categoryId);
				this.getCourseList();
			},
			getCourseList() {
				var _this = this;
				this.$http.courseList(this.categoryId)
					.then(function (res) {
						_this.courseList = res.data;
						// console.log(_this.categoryId)
						// console.log(_this.courseList)
					})
					.catch(err => {
						console.log(err)
					})
			},
            // 课程列表点击事件
            courseHandler(id){
                this.$router.push({
                    name:'course_detail',
                    params:{
                    	courseId:id,
                    }
                })
            }
		},
		created() {
			this.getCategoryList();
			this.getCourseList();
		},
	}
</script>

<style scoped>
    li {
        cursor: pointer;
    }

    li:active {
        color: chartreuse;
    }

    .course-list {
        padding-top: 20px;
    }

    .main {
        width: 1100px;
        margin: 0 auto;
        padding-top: 40px;
    }

    .screening {
        height: 190px;
        background-color: #fff;
        border-bottom: 1px solid #f6f6f6;
    }

    .ul1 p {
        height: 96px;
        float: left;
        margin: 23px 0 0 30px;
        display: inline-block;
    }

    .ul1 li {
        float: left;
        margin: 20px 0 0 10px;
        padding: 6px 15px;
        display: inline-block;
    }

    .ul1 li.active {
        color: #ffc210;
        box-shadow: 0 0 0 1px #ffc210 !important;
        border-radius: 30px;
    }

    .course-list {
        padding-top: 30px;
    }

    .course-list dl {
        height: 210px;
        background-color: #fff;
        margin: 0 0 35px;
        padding: 20px 30px 20px 20px;
        box-shadow: 2px 3px 16px rgba(0, 0, 0, .1);
        transition: all .2s ease;
    }

    .course-list dl dt {
        margin-right: 20px;
        float: left;
    }

    dt img {
        width: 423px;
        height: 210px;
    }

    .course-list dl dd {
        width: 597px;
        height: 210px;
        float: left;
    }
</style>