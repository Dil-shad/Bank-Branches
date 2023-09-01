#API for get bank details with the specific IFSC
curl -X GET "http://127.0.0.1:8000/bn/bank/?ifsc=ALLA0210807" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZXhwIjoxNjkzOTA1OTMzLCJpYXQiOjE2OTM0NzM5MzN9.GrIOqoeam_YfL5rZlsvQta_vgAsrFbzDY0Au0oHZloA"

# All Branches with pagination [?page=2]
curl -X GET "http://127.0.0.1:8000/bn/all-Banks-View/?page_size=12" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZXhwIjoxNjkzOTA1OTMzLCJpYXQiOjE2OTM0NzM5MzN9.GrIOqoeam_YfL5rZlsvQta_vgAsrFbzDY0Au0oHZloA"


# Filter bank details by bank name and city, including offset and limit.
curl -X GET "http://127.0.0.1:8000/bn/Get-Branch-details/?bank_name=state%20bank&city=tirur&limit=5&offset=0" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZXhwIjoxNjkzOTA1OTMzLCJpYXQiOjE2OTM0NzM5MzN9.GrIOqoeam_YfL5rZlsvQta_vgAsrFbzDY0Au0oHZloA"

