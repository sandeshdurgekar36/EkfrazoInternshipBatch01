import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';
import { ReviewService } from 'src/app/services/review.service'; 
import { Router } from '@angular/router';


@Component({
  selector: 'app-review',
  templateUrl: './review.component.html',
  styleUrls: ['./review.component.css']
})
export class ReviewComponent implements OnInit {
  
  constructor(private rService: ReviewService,private fb:FormBuilder,private router:Router) { }

  ngOnInit(): void {
    this.reviewform = new FormGroup({
      'review_stars':new FormControl(null, Validators.required),
      'review_type':new FormControl(null, Validators.required),
      'comments':new FormControl(null, Validators.required),
      'linked_id':new FormControl(null, Validators.required),
    });
  }
  get review_stars() {
    return this.reviewform.get('review_stars');
  }
  get review_type() {
    return this.reviewform.get('review_type');
  }
  get comments() {
    return this.reviewform.get('comments');
  }
  get linked_id() {
    return this.reviewform.get('linked_id');
  }
  reviewform = this.fb.group ({
    review_stars: ['',Validators.required],
    review_type: ['',Validators.required],
    comments: ['',Validators.required],
    linked_id: ['',Validators.required],
  })
  reviews(){
    console.log(this.reviewform.value)
    this.rService.reviews(this.reviewform.value).subscribe(response =>{
      alert("alert");
      console.log(response)
    })

  }
}
