import React, { Component } from 'react'
import axios from 'axios'
export default class Cinema extends Component {
    constructor() {
        super()
        // axios.get("").then(res=>{}).catch(err=>{console.log(err)})
        axios({
            url: "https://m.maizuo.com/gateway?k=7161035",
            method:"get",
            headers: {
                'X-Client-Info': '{ "a": "3000", "ch": "1002", "v": "5.2.1", "e": "16668849144401525434613761" }',
                'X-Host': 'mall.film-ticket.city.list'
            }
        }).then(res=>{
            console.log(res.data)
        })
    }
    render() {
        return (
            <div>Cinema</div>
        )
    }
}
