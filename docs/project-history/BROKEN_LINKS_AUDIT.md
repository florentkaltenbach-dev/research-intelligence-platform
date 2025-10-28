# Broken Links Audit - October 28, 2025

Comprehensive audit of broken internal links in the docs/ folder.

## Summary

**Total Broken Links Found**: 18
**Fixed**: 2
**Remaining**: 16 (require content creation or link removal)

---

## Fixed Links

### 1. `/events/central-bank-gold-2025`
**Status**: ✅ FIXED

**Issue**: File doesn't exist
**Correct Link**: `/events/central-bank-gold-accumulation-1000-tonnes-annually-for-three-consecutive-years`

**Fixed in**:
- `docs/events/saudi-pif-repositioning.md` (line 120)
- `docs/index.md` (line 26)

### 2. `/perspectives/indian/brics-payments-stance`
**Status**: ✅ FIXED

**Issue**: Specific perspective article doesn't exist
**Solution**: Removed link, kept quote as plain text
**Fixed in**: `docs/index.md` (line 30)

---

## Remaining Broken Links

### Category: Index/Navigation Links

#### `/events/`
**Type**: Bare link to index (should work if `docs/events/index.md` exists)
**Action**: Verify `/events/` resolves to `/events/index.md` in Jekyll

#### `/perspectives/`
**Type**: Bare link to perspectives index
**Action**: Verify Jekyll routing or change to `/perspectives/index`

#### `/historical-patterns/`
**Type**: Bare link to patterns index
**Action**: Verify Jekyll routing or change to `/historical-patterns/index`

---

### Category: Missing Regional Perspective Index Pages

These links point to regional perspective overview pages that don't exist as standalone files:

1. `/perspectives/african/` - Expected file: `docs/perspectives/african/index.md`
2. `/perspectives/chinese/` - Expected file: `docs/perspectives/chinese/index.md`
3. `/perspectives/indian/` - Expected file: `docs/perspectives/indian/index.md` (EXISTS, verify routing)
4. `/perspectives/middle-eastern/` - Expected file: `docs/perspectives/middle-eastern/index.md`
5. `/perspectives/russian/` - Expected file: `docs/perspectives/russian/index.md`
6. `/perspectives/western/` - Expected file: `docs/perspectives/western/index.md`

**Action Required**: These index files DO exist. Issue is likely Jekyll trailing slash routing. Test or change links to remove trailing slash.

---

### Category: Missing Specific Perspective Articles

1. `/perspectives/african/cips-adoption`
   - **Referenced in**: Unknown (needs grep)
   - **Action**: Create article or remove link

2. `/perspectives/central-banks/cbdc-vs-crypto`
   - **Referenced in**: Unknown
   - **Folder issue**: No `central-banks` folder exists
   - **Action**: Create folder + article or remove link

3. `/perspectives/chinese/bri-islamic-finance`
   - **Referenced in**: Unknown
   - **Action**: Create article or remove link

4. `/perspectives/chinese/yuan-internationalization`
   - **Referenced in**: Unknown
   - **Action**: Create article or remove link

5. `/perspectives/russian/sanctions-circumvention`
   - **Referenced in**: Unknown
   - **Action**: Create article or remove link

---

### Category: Missing Historical Pattern Files

Referenced patterns that need dedicated files:

1. `/historical-patterns/mamluk-ottoman`
   - **Pattern**: Mamluk-Ottoman Transition (1517) - Technology gap
   - **Action**: Create dedicated pattern file

2. `/historical-patterns/ming-qing`
   - **Pattern**: Ming-Qing Transition (1644) - Defection over conquest
   - **Action**: Create dedicated pattern file

3. `/historical-patterns/mongol-fragmentation`
   - **Pattern**: Mongol Empire Fragmentation - Competing alternatives
   - **Action**: Create dedicated pattern file

**Additional patterns mentioned but not yet linked**:
- British-American (1914-1944) - 30-year infrastructure transition
- Soviet Collapse (1991) - Internal contradictions
- British Slave Trade Abolition - Strategic retreat as moral progress
- Bretton Woods Creation (1944) - Post-war institutional architecture
- Petrodollar (1973) - Saudi-US energy-currency pact

---

## Recommendations

### Priority 1: Quick Fixes (Jekyll Routing)
Test whether trailing slashes in `/perspectives/` links work. If not:
- Find/replace `/perspectives/chinese/` with `/perspectives/chinese/index`
- Same for other regional indexes

### Priority 2: Create Missing Historical Patterns
High-value content referenced throughout. Create 8 pattern files:
1. `mamluk-ottoman-transition-1517.md`
2. `ming-qing-transition-1644.md`
3. `mongol-empire-fragmentation.md`
4. `british-american-transition-1914-1944.md`
5. `soviet-collapse-1991.md`
6. `british-slave-trade-abolition.md`
7. `bretton-woods-creation-1944.md`
8. `petrodollar-1973.md`

### Priority 3: Create or Remove Specific Perspective Links
Grep for files containing these links, then either:
- Create the referenced perspective articles
- Remove the links from source files

---

## Commands for Further Analysis

### Find all files containing specific broken links:
```bash
grep -r "/perspectives/african/cips-adoption" docs/ --include="*.md"
grep -r "/perspectives/chinese/yuan-internationalization" docs/ --include="*.md"
grep -r "/perspectives/russian/sanctions-circumvention" docs/ --include="*.md"
grep -r "/historical-patterns/mamluk-ottoman" docs/ --include="*.md"
```

### Verify Jekyll routing for trailing slashes:
```bash
cd docs/
bundle exec jekyll build --verbose
# Check _site/ output for how links resolve
```

---

## Notes

- Most broken links are to **content that should exist** based on references throughout the research
- Historical patterns are frequently mentioned but not extracted into dedicated files
- Perspective folder structure is messy (54 folders) but all have index.md files
- Consider consolidating perspective folders as separate refactoring task

---

**Audit Date**: October 28, 2025
**Auditor**: Claude Code
**Next Review**: After fixing Priority 1-2 items
