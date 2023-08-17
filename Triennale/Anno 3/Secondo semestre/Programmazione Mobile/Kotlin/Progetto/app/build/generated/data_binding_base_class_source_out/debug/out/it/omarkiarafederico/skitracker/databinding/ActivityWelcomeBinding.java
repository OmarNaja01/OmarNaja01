// Generated by view binder compiler. Do not edit!
package it.omarkiarafederico.skitracker.databinding;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.FrameLayout;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.fragment.app.FragmentContainerView;
import androidx.viewbinding.ViewBinding;
import androidx.viewbinding.ViewBindings;
import it.omarkiarafederico.skitracker.R;
import java.lang.NullPointerException;
import java.lang.Override;
import java.lang.String;

public final class ActivityWelcomeBinding implements ViewBinding {
  @NonNull
  private final ConstraintLayout rootView;

  @NonNull
  public final FragmentContainerView tutorialFragmentsContainerView;

  @NonNull
  public final FrameLayout welcome;

  private ActivityWelcomeBinding(@NonNull ConstraintLayout rootView,
      @NonNull FragmentContainerView tutorialFragmentsContainerView, @NonNull FrameLayout welcome) {
    this.rootView = rootView;
    this.tutorialFragmentsContainerView = tutorialFragmentsContainerView;
    this.welcome = welcome;
  }

  @Override
  @NonNull
  public ConstraintLayout getRoot() {
    return rootView;
  }

  @NonNull
  public static ActivityWelcomeBinding inflate(@NonNull LayoutInflater inflater) {
    return inflate(inflater, null, false);
  }

  @NonNull
  public static ActivityWelcomeBinding inflate(@NonNull LayoutInflater inflater,
      @Nullable ViewGroup parent, boolean attachToParent) {
    View root = inflater.inflate(R.layout.activity_welcome, parent, false);
    if (attachToParent) {
      parent.addView(root);
    }
    return bind(root);
  }

  @NonNull
  public static ActivityWelcomeBinding bind(@NonNull View rootView) {
    // The body of this method is generated in a way you would not otherwise write.
    // This is done to optimize the compiled bytecode for size and performance.
    int id;
    missingId: {
      id = R.id.tutorialFragmentsContainerView;
      FragmentContainerView tutorialFragmentsContainerView = ViewBindings.findChildViewById(rootView, id);
      if (tutorialFragmentsContainerView == null) {
        break missingId;
      }

      id = R.id.welcome;
      FrameLayout welcome = ViewBindings.findChildViewById(rootView, id);
      if (welcome == null) {
        break missingId;
      }

      return new ActivityWelcomeBinding((ConstraintLayout) rootView, tutorialFragmentsContainerView,
          welcome);
    }
    String missingId = rootView.getResources().getResourceName(id);
    throw new NullPointerException("Missing required view with ID: ".concat(missingId));
  }
}