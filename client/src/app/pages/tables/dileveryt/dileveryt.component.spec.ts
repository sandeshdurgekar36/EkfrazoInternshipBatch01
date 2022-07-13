import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DileverytComponent } from './dileveryt.component';

describe('DileverytComponent', () => {
  let component: DileverytComponent;
  let fixture: ComponentFixture<DileverytComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DileverytComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DileverytComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
