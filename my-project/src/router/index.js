import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home/Home'
import Course from "@/components/Course/Course";
import LightCourse from "@/components/LightCourse/LightCourse";
import Micro from "@/components/Micro/Micro";
import CourseDetail from "@/components/Course/CourseDetail";

Vue.use(Router)

export default new Router({
	linkActiveClass: 'is-active',
	routes: [
		{
			path: '/',
			redirect: {name: "Home"}
		},
		{
			path: '/home',
			name: 'Home',
			component: Home
		},
		{
			path: '/Course',
			name: 'Course',
			component: Course
		},
		{
			path: '/home/light-course',
			name: 'LightCourse',
			component: LightCourse
		},
		{
			path: '/micro',
			name: 'Micro',
			component: Micro
		},
		{
			path: '/course/:courseId/detail-introduce',
			name: 'course_detail',
			component: CourseDetail
		}
	]
})
