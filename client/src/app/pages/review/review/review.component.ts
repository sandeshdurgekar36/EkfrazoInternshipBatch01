import { Component, OnInit } from '@angular/core';
import { FormGroup,FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-review',
  templateUrl: './review.component.html',
  styleUrls: ['./review.component.css']
})
export class ReviewComponent implements OnInit {
  review!: FormGroup;

  constructor() { }

  ngOnInit(): void {
    this.review! = new FormGroup({
      'review_stars':new FormControl(null, Validators.required),
      'review_type':new FormControl(null, Validators.required),
      'comments':new FormControl(null, Validators.required),
      'linked_id':new FormControl(null, Validators.required),
      
      
      
      
      
    });
  }
  get review_stars() {
    return this.review!.get('review_stars');
  }
  get review_type() {
    return this.review!.get('review_type');
  }
  get comments() {
    return this.review!.get('comments');
  }
  get linked_id() {
    return this.review!.get('linked_id');
  }
}
