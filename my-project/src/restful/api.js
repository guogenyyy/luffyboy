import Axios from 'axios'

Axios.defaults.baseURL = 'https://www.luffycity.com/api/v1'
const categoryListUrl = '/course_sub/category/list/'
const courseListUrl = '/courses/?sub_category='
const courseDetailUrl = '/course/'

// https://www.luffycity.com/api/v1
export function categoryList() {
	return Axios.get(categoryListUrl).then(res => res.data)
}

export function courseList(categoryId) {
	return Axios.get(`${courseListUrl}${categoryId}&ordering=`).then(res => res.data)
}

export function courseDetail(courseId) {
	return Axios.get(`${courseDetailUrl}${courseId}/payment_info/`).then(res => res.data)
}

//基于Vue +django  restful 规范 前后端分离  CRUD的图书管理系统
//路飞整个业务介绍
//路飞 上线流程
//debug
//git

