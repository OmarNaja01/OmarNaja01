// Generated by view binder compiler. Do not edit!
package it.omarkiarafederico.skitracker.databinding;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.viewbinding.ViewBinding;
import androidx.viewbinding.ViewBindings;
import it.omarkiarafederico.skitracker.R;
import java.lang.NullPointerException;
import java.lang.Override;
import java.lang.String;

public final class FragmentGuida2Binding implements ViewBinding {
  @NonNull
  private final ConstraintLayout rootView;

  @NonNull
  public final ConstraintLayout guida2;

  @NonNull
  public final LinearLayout linearLayout;

  @NonNull
  public final Button secondTutorialBackBtn;

  @NonNull
  public final ImageView secondTutorialImg;

  @NonNull
  public final ImageView secondTutorialImg2;

  @NonNull
  public final ImageView secondTutorialImg3;

  @NonNull
  public final ImageView secondTutorialImg4;

  @NonNull
  public final ImageView secondTutorialImg5;

  @NonNull
  public final Button secondTutorialNextBtn;

  @NonNull
  public final TextView secondTutorialText;

  private FragmentGuida2Binding(@NonNull ConstraintLayout rootView,
      @NonNull ConstraintLayout guida2, @NonNull LinearLayout linearLayout,
      @NonNull Button secondTutorialBackBtn, @NonNull ImageView secondTutorialImg,
      @NonNull ImageView secondTutorialImg2, @NonNull ImageView secondTutorialImg3,
      @NonNull ImageView secondTutorialImg4, @NonNull ImageView secondTutorialImg5,
      @NonNull Button secondTutorialNextBtn, @NonNull TextView secondTutorialText) {
    this.rootView = rootView;
    this.guida2 = guida2;
    this.linearLayout = linearLayout;
    this.secondTutorialBackBtn = secondTutorialBackBtn;
    this.secondTutorialImg = secondTutorialImg;
    this.secondTutorialImg2 = secondTutorialImg2;
    this.secondTutorialImg3 = secondTutorialImg3;
    this.secondTutorialImg4 = secondTutorialImg4;
    this.secondTutorialImg5 = secondTutorialImg5;
    this.secondTutorialNextBtn = secondTutorialNextBtn;
    this.secondTutorialText = secondTutorialText;
  }

  @Override
  @NonNull
  public ConstraintLayout getRoot() {
    return rootView;
  }

  @NonNull
  public static FragmentGuida2Binding inflate(@NonNull LayoutInflater inflater) {
    return inflate(inflater, null, false);
  }

  @NonNull
  public static FragmentGuida2Binding inflate(@NonNull LayoutInflater inflater,
      @Nullable ViewGroup parent, boolean attachToParent) {
    View root = inflater.inflate(R.layout.fragment_guida2, parent, false);
    if (attachToParent) {
      parent.addView(root);
    }
    return bind(root);
  }

  @NonNull
  public static FragmentGuida2Binding bind(@NonNull View rootView) {
    // The body of this method is generated in a way you would not otherwise write.
    // This is done to optimize the compiled bytecode for size and performance.
    int id;
    missingId: {
      ConstraintLayout guida2 = (ConstraintLayout) rootView;

      id = R.id.linearLayout;
      LinearLayout linearLayout = ViewBindings.findChildViewById(rootView, id);
      if (linearLayout == null) {
        break missingId;
      }

      id = R.id.secondTutorialBackBtn;
      Button secondTutorialBackBtn = ViewBindings.findChildViewById(rootView, id);
      if (secondTutorialBackBtn == null) {
        break missingId;
      }

      id = R.id.secondTutorialImg;
      ImageView secondTutorialImg = ViewBindings.findChildViewById(rootView, id);
      if (secondTutorialImg == null) {
        break missingId;
      }

      id = R.id.secondTutorialImg2;
      ImageView secondTutorialImg2 = ViewBindings.findChildViewById(rootView, id);
      if (secondTutorialImg2 == null) {
        break missingId;
      }

      id = R.id.secondTutorialImg3;
      ImageView secondTutorialImg3 = ViewBindings.findChildViewById(rootView, id);
      if (secondTutorialImg3 == null) {
        break missingId;
      }

      id = R.id.secondTutorialImg4;
      ImageView secondTutorialImg4 = ViewBindings.findChildViewById(rootView, id);
      if (secondTutorialImg4 == null) {
        break missingId;
      }

      id = R.id.secondTutorialImg5;
      ImageView secondTutorialImg5 = ViewBindings.findChildViewById(rootView, id);
      if (secondTutorialImg5 == null) {
        break missingId;
      }

      id = R.id.secondTutorialNextBtn;
      Button secondTutorialNextBtn = ViewBindings.findChildViewById(rootView, id);
      if (secondTutorialNextBtn == null) {
        break missingId;
      }

      id = R.id.secondTutorialText;
      TextView secondTutorialText = ViewBindings.findChildViewById(rootView, id);
      if (secondTutorialText == null) {
        break missingId;
      }

      return new FragmentGuida2Binding((ConstraintLayout) rootView, guida2, linearLayout,
          secondTutorialBackBtn, secondTutorialImg, secondTutorialImg2, secondTutorialImg3,
          secondTutorialImg4, secondTutorialImg5, secondTutorialNextBtn, secondTutorialText);
    }
    String missingId = rootView.getResources().getResourceName(id);
    throw new NullPointerException("Missing required view with ID: ".concat(missingId));
  }
}