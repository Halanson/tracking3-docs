.. _project-settings-attribute:

=========
Attribute
=========

.. toctree::
   :maxdepth: 2


An **Attribute** is a property of an :doc:`/docs/Project/Settings/AssetDefinition/index` or in other words, if an :doc:`/docs/Project/Settings/AssetDefinition/index` is a table then an **Attribute** would be one column of that table.

.. image:: ./attribute.png
    :class: help-tip

The same :doc:`/docs/Project/Settings/AssetDefinition/index` can be used in many data grids, for example an :doc:`/docs/Project/Settings/AssetDefinition/index` 'Shot' can be used in multiple sequences to display many shots. They all have the same definition, but are different **Assets**.


-----
Label
-----
This is the label of your **Attribute** or column.


----
Type
----
There are many different types of **Attributes**, each for a different use case.


Asset Name
==========
This type shows the name or label of an row or asset. The colored bar shows the current state of other **Attributes** of type `State`_ in this data grid.

.. image:: ./type_assetName.png
    :class: help-tip


Duration
========
In a **Duration** type you can insert the length of a shot including the footage start, footage end, clip in and clip out.
As you can see in the example below the last shot has a source footage starting from frame 990 to frame 1170, with a total length of 181 frames. But the clip that actually will be used in production starts from frame 1001 to frame 1166, with a total length of 166 frames.

.. image:: ./type_duration.png
    :class: help-tip


Parent Asset
============

.. image:: ./type_parentAsset.png
    :class: help-tip


Parent Asset Source
-------------------
Here you can define dependencies between **Asset Definitions**. For example an :doc:`/docs/Project/Settings/AssetDefinition/index` 'Shot' belongs to an :doc:`/docs/Project/Settings/AssetDefinition/index` 'Sequence'. Using the **Type Parent Asset** you can achieve this.

In the example you can see a data grid for the :doc:`/docs/Project/Settings/AssetDefinition/index` 'Shot' with an **Attribute** called 'Sequence'. This **Attribute** 'Sequence' is of the type of **Parent Asset** and pointing to the **Main Attribute** of an :doc:`/docs/Project/Settings/AssetDefinition/index` called 'Sequence'.


State
=====
With this type you can show the different states of a single process in production.

.. image:: ./type_state.png
    :class: help-tip


Text
====
This is useful for some general notes or descriptions.

.. image:: ./type_text.png
    :class: help-tip


-----
Width
-----
Is the width of an **Attribute** column it has by default in a data grid.


------
Pinned
------
You can pin **Attributes** to the left or right side of a data grid. Pinned **Attributes** will always be visible, even on large data grids.
