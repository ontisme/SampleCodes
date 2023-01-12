#### 自動補全 Auto Complete
```
<template>
   <el-autocomplete
        v-model="searchInfo.user_id"
        :fetch-suggestions="querySearch"
        placeholder="輸入用戶名會提示ID"
    />
</template>


// 模糊搜尋，關鍵重點是 array 內 一定都要有名為 "value" 的 key
// 0: {value: "admin"}
// 1: {value: "user"}
<script setup>

  const userDatas = ref([])
  const querySearch = (queryString, cb) => {
    let new_data_list = []
    userDatas.value.filter((item) => {
      if (item.userName.indexOf(queryString) !== -1) {
        new_data_list.push({
          value:item.ID
        })
      }
    })
    // call callback function to return suggestions
    console.log(new_data_list)
    cb(new_data_list)
  }
</script>
```
